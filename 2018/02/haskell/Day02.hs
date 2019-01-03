module Main where

import Data.List (group, sort)

main :: IO ()
main = do
  file <- readFile "../ids.txt"
  let ids = lines file
  print $ "Answer part one: " ++ show (checksum ids)

checksum :: [String] -> Int
checksum ids = pairs * triples
  where
    pairs = length $ filter (any ((== 2) . length)) grouped
    triples = length $ filter (any ((== 3) . length)) grouped

    grouped = map (group . sort) ids
