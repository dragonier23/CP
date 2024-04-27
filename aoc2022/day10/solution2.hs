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
parse = map (parseDecide . words) . lines

parseDecide :: [String] -> (String, Int)
parseDecide ("noop":xs) = ("noop", 0)
parseDecide ("addx":val:xs) = ("addx", read val)

solution :: [(String, Int)] -> String
solution xs = unlines . parseSolution . reverse $ foldl (\acc x -> (solutionDecide x acc):acc) [] (take 240 . reverse . foldl action [1] $ xs)

action :: [Int] -> (String, Int) -> [Int]
action all@(x:xs) ("noop", _) = x:all
action all@(x:xs) ("addx", val) = (x+val):x:all

solutionDecide :: Int -> [Char] -> Char
solutionDecide spritePos xs = if crtPos `elem` acceptablePos then '#' else '.'
  where crtPos = length xs `mod` 40
        acceptablePos = [spritePos, spritePos - 1, spritePos + 1]


parseSolution :: String -> [String]
parseSolution [] = []
parseSolution xs = take 40 xs : parseSolution (drop 40 xs)
