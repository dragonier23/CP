-- main = putStrLn "Hello World!"

-- type of putStrLn: putStrLn :: String -> IO ()
-- returns an IO action that has a result type of ()
-- IO action is something that will carry out an action with a side effect and contain some return 
-- value inside it 

-- an IO action will be performed when we give it the name of main and run the program. 
-- we can also include more IO actions with the do syntax 
{-
main = do 
    putStrLn "Hello, your name is"
    name <- getLine
    putStrLn $ "Hello " ++ name 
-}
-- :t getLine -> getLine :: IO String 
-- carry out the action of reading from the terminal, and the input will be represented as a String
-- the <- notation means that the value in the IO action is bound to "name"
-- = will not work, we can think about getLine as a function, and that name will just be another name
-- for the function getLine

-- IO action can also be thought as a box that goes into the impure world, does something and 
-- returns with a value (significant or not)
-- only <- construct can retrieve the value from this box
-- we note that we can only "take out" data from an IO action when we are in another IO action 

-- binding it to name "untaints" the value temperatrily 

-- we can technically bind the first line too: foo <- putStrLn "Hello, your name is", but foo would
-- just be (), which is pointless 

-- we also note that the last action in a do block cannot be bound to a name
-- I/O actions will only be performed when they are given a name of main or when they're inside a 
-- bigger I/O action that we composed with a do block. We can also use a do block to glue together 
-- a few I/O actions and then we can use that I/O action in another do block and so on. Either way, 
-- they'll be performed only if they eventually fall into main.

-- let bindings can help us handle our pure expressions in the unpure main function
{-
main = do 
    putStrLn "What's your first name?"
    firstName <- getLine
    putStrLn "What's your last name?"
    lastName <- getLine
    let bigFirstName = map toUpper firstName
        bigLastName = map toUpper lastName
    putStrLn $ "hey " ++ bigFirstName ++ " " ++ bigLastName ++ ", how are you?"
-}
-- Note: we need to line out the let bindings, and use it to bind pure expressions to names 

-- programme that continousely reads a line and prints out the same line with the words reversed

{- 
main = do 
    line <- getLine
    if null line
        then return () -- we basically have to return some IO value for each branch 
        else do
            putStrLn $ reverseWords line 
            main 

reverseWords :: String -> String  
reverseWords = unwords . map reverse . words 
--}

-- we can use runhaskell inputoutput.hs to compile the file on the fly 
-- we note that the return type of main is essentially an IO action, hence, do blocks have the
-- structure if condition then IO action else IO action 
-- the else part requires the do notation because we have to have exactly 1 IO action after the else
-- so we "glue" the 2 IO actions tgt with the do block

-- return takes a pure value and makes it an IO action (when evoked in IO actions)
-- in this case, it does not end the execution of the function prematurely 
-- it could be treated as the opposite to <- 

{-
When dealing with I/O do blocks, we mostly use return either because we need to create an I/O action 
that doesn't do anything or because we don't want the I/O action that's made up from a do block to 
have the result value of its last action, but we want it to have a different result value, so we use 
return to make an I/O action that always has our desired result contained and WE PUT IT IN THE END.
-}

-- MAIN USER OUTPUT
-- putStrLn
-- putStr dosent skip to the next line , putChar for char, print = putStrLn . show (need value to 
-- be part of show typeclass)

{-
putStr :: String -> IO ()
putStr [] = return ()
putStr x:xs = do putChar x 
                 putStr xs
-}

-- MAIN USER INPUT
-- getLine, getChar, getContents

{-
main = do 
    c <- getChar 
    if c == ' '
        then return ()
        else do 
            putChar c 
            main 
-}

-- we would expect them to take just 1 character, but it dosent really execute until we hit return 
-- the "when" function can help us to simplify this code: it is a function that takes a boolean value
-- and an IO action. if boolean true, it returns the IO action, otherwise, it returns "return ()"

{-
import Control.Monad 

main = do
    c <- getChar
    when (c /= ' ') $ do
        putChar c
        main -}

--useful when we want to have the "if something do something else return () pattern"

-- sequence takes a list of IO actions and returns an IO action that will perform all the IO actions
-- :t sequence is [IO a] -> IO [a]

{-
main = do
    a <- getLine
    b <- getLine
    c <- getLine
    print [a,b,c] 
is the same as 

main = do
    rs <- sequence [getLine, getLine, getLine]
    print rs 
-}

-- common pattern is to use sequence when we map functions like print over list
-- i.e. sequence (map print [1..4])
-- in GHCi, this will also print [(), (), (), ()], as it prints all IO actions unless it is ()

-- mapM takes a function and a list, maps the function over the list and sequences it. 
-- mapM_ does the same, but throws aways the result 
-- forecer takes an IO action and returns an IO action that repeats the IO action forever. To use this, 
-- import
import Control.Monad 

-- forM is like mapM, but with input swapped 
-- this allows for us to do things like 

{-
main = do 
    colors <- forM [1..4] (\a -> do 
        putStrLn $ "Which color do you associate with the number " ++ show a ++ "?"
        color <- getLine
        return color)
    putStrLn "The colors that you associate with 1, 2, 3 and 4 are: "
    mapM putStrLn colors
-}

-- getContents reads line from stdin, until it encounters an EOF char (we can do ctrl-d to manually create EOF)
-- :t getContents is IO String
-- makes it easy to use piping, and essentially is like getLine
-- e.g.
import Data.Char
{-
main = do 
    contents <- getContents
    putStr (map toUpper contents)
    -- vs print contents -}
-- we note print essentially is putStrLn . show, so it includes the "" whereas putStr dosent, 
-- it needs us to feed a string so it wont have the "" 

{-
main = do 
    contents <- getContents 
    putStrLn (shortLinesOnly contents)

shortLinesOnly :: String -> String 
shortLinesOnly input = unlines . filter (\line -> length line < 10) . lines $ input 
  -}  

-- theres also a function to do this: "interact". It takes a function and retruns and Io action taking
-- some input, runs that function and prints the output. 
-- main = interact $ unlines . filter ((<10) . length) . lines 
-- Note: :t interact is String -> String 

-- function to check if input is a palidrome 
    {-
checkPalindrome :: String -> String
checkPalindrome input = unlines . map (\x -> if x == (reverse x) then "True" else "False") $ lines input  

main = interact checkPalindrome-}

import System.IO
{-
What about reading from a file. Consider the following
main = do 
    handle <- openFile "Girlfriend.txt" ReadMode
    contents <- hGetContents handle
    putStr contents
    hClose handle

here we note: 
1. openFile :: FilePath -> IOMode -> IO Handle
- FilePath is a type synonym for string
- IOMode is defined: data IOMode = ReadMode | WriteMode | AppendMode | ReadWriteMode
- it returns an IO action that will open the specified file in the specified mode, bound to a handle 
- this rep where the file is located, and is like a memory address 
2. hGetContents - similar to getContents, except it take handle as a parameter and reads from the file, 
not stdin
3. hClose: takes a handle and returns an IO action which closes the file (NOTE NEED TO DO)

-}
