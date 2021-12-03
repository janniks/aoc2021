use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let input = read_lines("../input/day01.txt");
    let measurments: Vec<i16> = input
        .lines()
        .map(|x| x.unwrap().parse::<i16>().unwrap())
        .collect();
    let increases = measurments
        .windows(4)
        .map(|v| (v.iter().take(3).sum(), v.iter().rev().take(3).sum()))
        .map(|(a, b): (i16, i16)| b - a)
        .filter(|x| x > &0)
        .count();

    println!("Number of sliding-window increases: {:?}", increases);
}

fn read_lines<P>(filename: P) -> io::BufReader<File>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).unwrap();
    io::BufReader::new(file)
}
