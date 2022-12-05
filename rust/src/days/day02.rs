use crate::{Solution, SolutionPair};
use std::fs::read_to_string;
use std::collections::HashMap;

///////////////////////////////////////////////////////////////////////////////

const points: HashMap<&'static str, i32> = HashMap::from([
    ("X", 1),
    ("Y", 2),
    ("Z", 3),
]);

pub fn solve() -> SolutionPair {
    let input: Vec<String> = read_to_string("input/day02.txt").unwrap()
        .lines()
        .map(str::to_string)
        .collect();

    for game_str in input {
        let opponent_choice = game_str.chars().;
        let my_choice = game_str[2];
    }

    let sol1: u64 = 0;
    let sol2: u64 = 0;

    (Solution::U64(sol1), Solution::U64(sol2))
}
