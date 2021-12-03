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
        .iter()
        .zip(measurments.iter().skip(1))
        .map(|(a, b)| b - a)
        .filter(|x| x > &0)
        .count();

    println!("Number of increases: {:?}", increases);
}

fn read_lines<P>(filename: P) -> io::BufReader<File>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).unwrap();
    io::BufReader::new(file)
}
