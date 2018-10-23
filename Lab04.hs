tree = Node Black 4 (Node Black 3 (Node Red 1 Nil Nil) Nil) (Node Red 11 (Node Black 7 (Node Red 6 Nil Nil) (Node Red 9 Nil Nil)) (Node Black 13 Nil Nil))

data Colour = Red | Black deriving (Show)

data RBTree = Nil | Node Colour Int RBTree RBTree deriving (Show)

searchRBTree :: RBTree -> Int -> Bool
searchRBTree Nil _ = False
searchRBTree (Node _ x lTree rTree) y | x == y = True
                                      | y <= x = searchRBTree lTree y
                                      | y > x  = searchRBTree rTree y

insertRBTree :: RBTree -> Int -> RBTree
insertRBTree Nil y = Node Red y Nil Nil
insertRBTree (Node col x lTree rTree) y | y == x = Node col x lTree rTree
                                        | y <  x = balance $ Node col x (insertRBTree lTree y) rTree
                                        | y >  x = balance $ Node col x lTree (insertRBTree rTree y)

balance :: RBTree -> RBTree
balance t = t
