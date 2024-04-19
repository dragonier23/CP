import System.IO
import Data.List
import qualified Data.Set as Set 
import Data.Char 

main = do 
    handle <- openFile  "problemstatement.txt" ReadMode --"test1.txt" ReadMode --
    contents <- hGetContents handle 
    let parsedContents = parse contents
        answer = solution parsedContents
    print answer
    hClose handle 

parse :: String -> [(String, String)]
parse = map (\line -> let n = div (length line) 2 
    in (take n line, reverse . take n . reverse $ line)) . lines

solution :: [([Char], [Char])] -> Int
solution = sum . map (\(firstCompartment, secondCompartment) -> 
    let firstSet = Set.fromList firstCompartment
        secondSet = Set.fromList secondCompartment
    in convert $ Set.toList (Set.intersection firstSet secondSet))

convert :: [Char] -> Int
convert [x] 
    | x `elem` ['a'..'z'] = convert' smallCase x
    | otherwise = convert' largeCase x
    where 
        smallCase = elemIndex x ['a'..'z'] 
        largeCase = elemIndex x ['A'..'Z']

convert' :: Maybe Int -> Char -> Int
convert' Nothing x = 0
convert' (Just a) x 
    | x `elem` ['a'..'z'] = a + 1 
    | otherwise = a + 27 
