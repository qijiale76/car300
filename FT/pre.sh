#!/bin/sh
python data_pre.py p
python data_pre.py n
head -400 positive_print_500.txt > positive_400.txt
head -400 negative_print_500.txt > negative_400.txt
tail -100 negative_print_500.txt > negative_100.txt
tail -100 positive_print_500.txt > positive_100.txt
cat positive_400.txt negative_400.txt >train.txt
cat positive_100.txt negative_100.txt >exam.txt
rm positive_print_500.txt negative_print_500.txt positive_400.txt negative_400.txt positive_100.txt negative_100.txt

../fastText/fasttext supervised -input train.txt -output model
../fastText/fasttext test model.bin exam.txt

../fastText/fasttext predict model.bin exam.txt >temp1.txt
echo "100 should be positive:" 
head -100 temp1.txt | sort | uniq -c
echo "100 should be nagative:" 
tail -100 temp1.txt | sort | uniq -c

rm exam.txt model.bin model.vec train.txt temp1.txt