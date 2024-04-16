import System.IO
import Data.List

main = do 
    handle <- openFile  "problemstatement.txt" ReadMode --"test1.txt" ReadMode --
    contents <- hGetContents handle 
    let parsedContents = parse contents
        solutions = solution parsedContents
    print solutions
    hClose handle 

parse  :: String -> [[String]]
parse input = filter (\xs -> not(foldl (\acc x -> null x || acc) False xs)) . groupBy (\x y -> (null x) == (null y)) . lines $ input


solution :: (Num b, Read b, Ord b) => [[String]] -> b
solution xs = sum . take 3 . reverse . sort . map (sum . map read) $ xs
