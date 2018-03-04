#! /usr/bin/python

import unittest
import random
from tdd import f1,f2,f3,f4,f5,f6,f7

class TestTddF1(unittest.TestCase):

	def test_f1_1(self):
		w=f1(0)
		self.assertEqual(w,0)

        def test_f1_2(self):
                w=f1(1)
                self.assertEqual(w,1)

	def test_f1_3(self):
		w=f1(2)
		self.assertEqual(w,4)

	def test_f1_4(self):
		w=f1(2,1)
		self.assertEqual(w,5)

	def test_f1_5(self):
		w=f1(2,3)
		self.assertEqual(w,7)

class TestTddF2(unittest.TestCase):

	def test_f2_1(self):
		w=f2('ala')
		self.assertEqual(w,'a')

	def test_f2_2(self):
		w=f2([1,2,3])
		self.assertEqual(w,1)

	def test_f2_3(self):
		w=f2([])
		self.assertEqual(w,'BUUUUM')

class TestTddF3(unittest.TestCase):
	
	def test_f3_1(self):
		w=f3(1)
		self.assertEqual(w,'jeden')

	def test_f3_2(self):
		w=f3(2)
		self.assertEqual(w,'dwa')

	def test_f3_3(self):
		w=f3(3)
		self.assertEqual(w,'trzy')

	def test_f3_4(self):
		w=f3(random.choice(range(4,1000)))
		self.assertEqual(w,'other')

class TestTddF4(unittest.TestCase):
	
	def test_f4_1(self):
		w=f4('ala')
		self.assertEqual(w,'ala ma kota')

	def test_f4_2(self):
		w=f4('kot')
		self.assertEqual(w,'kot ma kota')

	def test_f4_3(self):
		w=f4('kot','psa')
		self.assertEqual(w,'kot ma kota i psa')

	def test_f4_4(self):
		w=f4('kot','mysz')
		self.assertEqual(w,'kot ma kota i mysz')

class TestTddF5(unittest.TestCase):
	
	def test_f5_1(self):
		w=f5(0)
		self.assertEqual(w,[])

        def test_f5_2(self):
                w=f5(1)
                self.assertEqual(w,[0])

        def test_f5_3(self):
                w=f5(2)
                self.assertEqual(w,[0,1])

        def test_f5_4(self):
                w=f5(7)
                self.assertEqual(w,[0,1,2,3,4,5,6])

        def test_f5_5(self):
                w=f5(7,2)
                self.assertEqual(w,[0,2,4,6])

        def test_f5_6(self):
                w=f5(17,2)
                self.assertEqual(w,[0,2,4,6,8,10,12,14,16])

        def test_f5_7(self):
                w=f5(17,5)
                self.assertEqual(w,[0,5,10,15])

class TestTddF6(unittest.TestCase):

	def test_f6_1(self):
		w=f6(1,'*')
		self.assertEqual(w,'*')

	def test_f6_2(self):
		w=f6(7,'*')
		self.assertEqual(w,'*******')

class TestTddF7(unittest.TestCase):
	
	def test_f7_1(self):
		w=f7('ala')
		self.assertEqual(w,'slowo')

        def test_f7_2(self):
                w=f7(1)
                self.assertEqual(w,'cyfra')

        def test_f7_3(self):
                w=f7(11111)
                self.assertEqual(w,'liczba')

        def test_f7_4(self):
                w=f7(-11111)
                self.assertEqual(w,'liczba_ze_znakiem')

        def test_f7_5(self):
                w=f7('Ala ma kota.')
                self.assertEqual(w,'zdanie')

        def test_f7_6(self):
                w=f7('<taaag>')
                self.assertEqual(w,'tag poczatkowy')

        def test_f7_7(self):
                w=f7('</taaag>')
                self.assertEqual(w,'tag koncowy')


if __name__ == '__main__':
	unittest.main()
