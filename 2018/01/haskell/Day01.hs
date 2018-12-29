module Main where

import Data.List
import qualified Data.Set as Set

main :: IO ()
main = do
  file <- readFile "../frequencies.txt"

  -- The '+' signs need to be removed for parsing to work.
  let fs = map ((read :: String -> Int) . delete '+') (lines file)

  print $ "Answer part one: " ++ show (sum fs)
  print $ "Answer part two: " ++ show (firstDup $ scanl (+) 0 $ cycle fs)

firstDup :: Ord a => [a] -> a
firstDup fs = dup fs Set.empty
  where
    dup (x:xs) s = if Set.member x s
                    then x
                    else dup xs (Set.insert x s)
