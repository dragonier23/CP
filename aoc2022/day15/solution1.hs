import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char
import Data.Function

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsed = parse contents
        answer = solution 2000000 parsed
        present =  countBeacon parsed
    print (answer - present) -- parsed --
    hClose handle

parse :: String -> [(Int, Int, Int, Int)] 
parse = map ((\x -> (read . drop 2 . init $ (x !! 4), read . drop 2 . init $ (x !! 6), read . drop 2 . init $ (x !! 16), read . drop 2 $ (x !! 18))) . groupBy ((==) `on` isSpace)) .
        lines

solution :: Int -> [(Int, Int, Int, Int)] -> Int
solution row = extract3 . settle . sort . foldl (\acc (sx, sy, bx, by) ->
                let dist = abs (sx - bx) + abs (sy - by)
                    remainder = dist - abs (row - sy)
                in  if remainder > 0 then (sx - remainder, sx + remainder):acc else acc) []

settle :: [(Int, Int)] -> (Int, Int, Int)
settle ((sx, sy):xs) = foldl (\(count, start, end) (nextStart, nextEnd) -> if nextStart <= end then (if nextEnd <= end then (count, start, end) else (count + nextEnd - end, start, nextEnd)) else (count + nextEnd - nextStart + 1, nextStart, nextEnd)) (sy - sx + 1, sx, sy) xs

extract3 :: (Int, Int, Int) -> Int
extract3 (x, _, _) = x

countBeacon :: [(Int, Int, Int, Int)] -> Int
countBeacon = foldl (\acc (_, yPos) -> if yPos == 2000000 then acc + 1 else acc) 0 . nub .  map (\(_, _, x, y) -> (x, y))  