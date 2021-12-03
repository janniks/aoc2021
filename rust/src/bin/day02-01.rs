use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

static UP: &str = "up";
static DOWN: &str = "down";
static FORWARD: &str = "forward";

fn main() {
    let direction = HashMap::from([
        (UP.to_string(), 0),
        (DOWN.to_string(), 1),
        (FORWARD.to_string(), 2),
    ]);
    let mut state = vec![0, 0, 0];

    let input = read_lines("../input/day02.txt");

    let measurments: Vec<Vec<String>> = input
        .lines()
        .map(|x| x.unwrap())
        .map(|x| x.split(' ').map(|x| x.to_string()).collect())
        .collect();

    let instructions: Vec<(&String, i32)> = measurments
        .iter()
        .map(|x| (&x[0], x[1].parse::<i32>().unwrap()))
        .collect();

    for line in instructions {
        state[direction[line.0]] += line.1;
    }

    let final_depth = state[direction[DOWN]] - state[direction[UP]];
    println!(
        "Final answer: {:?}",
        state[direction[FORWARD]] * final_depth
    )
}

fn read_lines<P>(filename: P) -> io::BufReader<File>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).unwrap();
    io::BufReader::new(file)
}
