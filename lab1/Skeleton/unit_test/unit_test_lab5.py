import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import BinaryHeap
import BookStore


class  BinaryHeapTest(unittest.TestCase) :
    
    def test_binaryheap(self) :
        points = 0.5
        q = BinaryHeap.BinaryHeap()
        try:
            a = q.remove()
        except IndexError:
            points += 0.5
            
        try:
            q.add(2)
            q.add(1)
            q.add(5)
            self.assertAlmostEqual(q.size(), 3)
            self.assertAlmostEqual(q.remove(), 1)
            q.add(4)
            q.add(1)
            q.add(3)
            self.assertAlmostEqual(q.size(), 5)
            self.assertAlmostEqual(q.remove(), 1)
            self.assertAlmostEqual(q.remove(), 2)
            self.assertAlmostEqual(q.remove(), 3)
            self.assertAlmostEqual(q.remove(), 4)
            self.assertAlmostEqual(q.remove(), 5)
            points += 1
        except:
            print("BinaryHeap is not correct")
        finally:
       
            print(f"BinaryHeap: {points} Points")
     
    def test_BookStore(self) :
        points = 0.5
        try:
            a = BookStore.BookStore()
            a.loadCatalog("../books.txt")
            points += 0.5
            a.searchBookByInfix("World of Po")

            
            points += 1
        except:
            print("BookStore is not correct")
        finally:
            print(f"BookStore: {points} Points")
    
    