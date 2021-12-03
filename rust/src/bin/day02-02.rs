use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

const UP: &str = "up";
const DOWN: &str = "down";
const FORWARD: &str = "forward";

fn main() {
    let input = read_lines("../input/day02.txt");

    let measurments: Vec<Vec<String>> = input
        .lines()
        .map(|x| x.unwrap())
        .map(|x| x.split(' ').map(|x| x.to_string()).collect())
        .collect();

    let instructions: Vec<(&str, i32)> = measurments
        .iter()
        .map(|x| (&*x[0], x[1].parse::<i32>().unwrap()))
        .collect();

    let mut aim = 0;
    let mut horizontal_position = 0;
    let mut depth = 0;

    for x in instructions {
        match x {
            (UP, y) => aim -= y,
            (DOWN, y) => aim += y,
            (FORWARD, y) => {
                horizontal_position += y;
                depth += aim * y
            }
            _ => (),
        }
    }

    println!("Final answer: {:?}", horizontal_position * depth)
}

fn read_lines<P>(filename: P) -> io::BufReader<File>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).unwrap();
    io::BufReader::new(file)
}
