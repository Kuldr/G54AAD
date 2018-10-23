tree = Node Black 4 (Node Black 3 (Node Red 1 Nil Nil) Nil) (Node Red 11 (Node Black 7 (Node Red 6 Nil Nil) (Node Red 9 Nil Nil)) (Node Black 13 Nil Nil))

data Colour = Red | Black deriving (Show)

data RBTree = Nil | Node Colour Int RBTree RBTree deriving (Show)

searchRBTree :: RBTree -> Int -> Bool
searchRBTree Nil _ = False
searchRBTree (Node _ x lTree rTree) y | x == y = True
                                      | y <= x = searchRBTree lTree y
                                      | y > x  = searchRBTree rTree y

insertRBTree :: RBTree -> Int -> RBTree
insertRBTree t y = blackRootRBTree $ insRBTree t y

blackRootRBTree :: RBTree -> RBTree
blackRootRBTree (Node col x t1 t2) = Node Black x t1 t2

insRBTree :: RBTree -> Int -> RBTree
insRBTree Nil y = Node Red y Nil Nil
insRBTree (Node col x lTree rTree) y | y == x = Node col x lTree rTree
                                        | y <  x = balance $ Node col x (insRBTree lTree y) rTree
                                        | y >  x = balance $ Node col x lTree (insRBTree rTree y)

balance :: RBTree -> RBTree
-- Black left Red left Red
balance (Node Black x3 (Node Red x2 (Node Red x1 t1 t2) t3) t4) = Node Red x2 (Node Black x1 t1 t2) (Node Black x3 t3 t4)
-- Black left Red right Red
balance (Node Black x3 (Node Red x1 t1 (Node Red x2 t2 t3)) t4) = Node Red x2 (Node Black x1 t1 t2) (Node Black x3 t3 t4)
-- Black right Red left Red
balance (Node Black x1 t1 (Node Red x3 (Node Red x2 t2 t3) t4)) = Node Red x2 (Node Black x1 t1 t2) (Node Black x3 t3 t4)
-- Black right Red right Red
balance (Node Black x1 t1 (Node Red x2 t2 (Node Red x3 t3 t4))) = Node Red x2 (Node Black x1 t1 t2) (Node Black x3 t3 t4)
balance t = t 
