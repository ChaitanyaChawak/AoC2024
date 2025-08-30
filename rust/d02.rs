use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file_path = "/home/chai/Documents/AoC2024/puzzles/d02.txt"; 

    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut count = 0.0;
    let mut count2 = 0.0;

    for line in reader.lines() {
        let line2 = line?;

        let mut columns: Vec<i32> = line2.split_whitespace().filter_map(|num| num.parse().ok()).collect();

        // println!("{:?}", columns);

        if checksafe(&columns) {
            count += 1.0;
        }

        for i in 0..columns.len() {
            let removed = columns.remove(i);

            if checksafe(&columns) {
                count2 += 1.0;
                break;
            }
            columns.insert(i, removed);

        }

    }

    println!("Part1: {}", count);
    println!("Part2: {}", count2);

    Ok(())
}

fn checksafe(numbers: &[i32]) -> bool {
    numbers.windows(2).all(|w| w[0] < w[1] && (w[1] - w[0]) <= 3 && (w[1] - w[0]) >= 1) ||
    numbers.windows(2).all(|w| w[1] < w[0] && (w[0] - w[1]) <= 3 && (w[0] - w[1]) >= 1)

}
