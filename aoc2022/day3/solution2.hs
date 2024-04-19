import System.IO
import Data.List
import qualified Data.Set as Set 
import Data.Char 

main = do 
    handle <- openFile "problemstatement.txt" ReadMode --"test1.txt" ReadMode -- 
    contents <- hGetContents handle 
    let parsedContents = parse (lines contents)
        answer = solution parsedContents
    print answer
    hClose handle 

parse :: [String] -> [(String, String, String)]
parse [] = []
parse (x:y:z:xs) = (x, y, z) : parse xs

solution :: [(String, String, String)] -> Int
solution = sum . map (\(firstElf, secondElf, thirdElf) -> 
    let firstSet = Set.fromList firstElf
        secondSet = Set.fromList secondElf
        thirdSet = Set.fromList thirdElf
    in convert $ Set.toList . Set.intersection thirdSet $ Set.intersection firstSet secondSet)

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
