use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let input = read_lines("../input/day03.txt");
    let logs: Vec<Vec<bool>> = input
        .lines()
        .map(|x| x.unwrap().chars().map(|x| x != '0').collect())
        .collect();

    let mut state = [0; 12];

    for item in logs {
        for (j, flag) in item.iter().enumerate() {
            state[j] += if *flag { 1 } else { -1 }
        }
    }

    let gamma_rate = isize::from_str_radix(
        state
            .iter()
            .map(|x| if x > &0 { '1' } else { '0' })
            .collect::<String>()
            .as_str(),
        2,
    )
    .unwrap();

    let epsilon_rate = gamma_rate ^ 0b111111111111;

    println!("Output: {:?}", gamma_rate * epsilon_rate);

    // try bit shifting instead
}

fn read_lines<P>(filename: P) -> io::BufReader<File>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).unwrap();
    io::BufReader::new(file)
}
