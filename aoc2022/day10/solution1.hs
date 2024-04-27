import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    --handle <- openFile "test2.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsedContents = parse contents
        answer = solution parsedContents
    print answer --parsedContents --answer
    hClose handle

parse :: String -> [(String, Int)]
parse = map (\x -> parseDecide . words $ x) . lines

parseDecide :: [String] -> (String, Int)
parseDecide ("noop":xs) = ("noop", 0)
parseDecide ("addx":val:xs) = ("addx", read val)

solution :: [(String, Int)] -> Int
solution xs = sum [(allStates !! (pos - 1)) * pos | pos <- [20, 60, 100, 140, 180, 220]]
  where allStates = reverse . foldl (\acc x -> action acc x) [1] $ xs

action :: [Int] -> (String, Int) -> [Int]
action all@(x:xs) ("noop", _) = x:all
action all@(x:xs) ("addx", val) = (x+val):x:all

