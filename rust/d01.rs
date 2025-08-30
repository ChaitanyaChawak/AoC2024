use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file_path = "/home/chai/Documents/AoC2024/puzzles/d01.txt"; 

    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut column1: Vec<f64> = Vec::new();
    let mut column2: Vec<f64> = Vec::new();

    for line in reader.lines() {
        let line2 = line?;

        let columns: Vec<&str> = line2.split_whitespace().collect();

        if columns.len() == 2 {
            let num1: f64 = match columns[0].parse() {
                Ok(n) => n,
                Err(_) => {
                    println!("Failed to parse number: {}", columns[0]);
                    continue;
                }
            };
            let num2: f64 = match columns[1].parse() {
                Ok(n) => n,
                Err(_) => {
                    println!("Failed to parse number: {}", columns[1]);
                    continue;
                }
            };

            column1.push(num1);
            column2.push(num2);
        }
    }

    column1.sort_by(|a, b| a.partial_cmp(b).unwrap());
    column2.sort_by(|a, b| a.partial_cmp(b).unwrap());

    let mut total_diff = 0.0;
    if column1.len() == column2.len() {
        for (num1, num2) in column1.iter().zip(column2.iter()) {
            let difference = (num1 - num2).abs();
            total_diff += difference;
        }
        println!("Part1: {}", total_diff);
    }

    let mut total_similarity = 0.0;
    for num1 in &column1 {
        let count = column2.iter().filter(|&&x| x == *num1).count();
        let similarity = num1*count as f64;
        total_similarity += similarity;
    }
    println!("Part2: {}", total_similarity);

    Ok(())
}