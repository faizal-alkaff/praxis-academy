###### Judul : Dasar-dasar Pemrograman Python (2)
###### Oleh : Muhammad Faizal Al Kaff
###### Tanggal : 3 Desember 2019
###### Ringkasan Materi : Pemrograman python dasar
###### Penjelasan Tentang Isi Repo : Implementasi dari Algoritma Sorting

## Daftar file hasil implementasi :
1. bubble_sort.py -> implementasi dari Algoritma Bubble Sort
	- call_bubbleSort.py -> cara menggunakan module bubble_sort.py
	```python
	import bubble_sort

	nlist = [14,46,43,27,57,41,45,21,70]
	bubble_sort.bubbleSort(nlist)
	```
	
	```
	Output :
	[2019-12-04 22:06.10]  /drives/c/Users/HP/Documents/praxis-academy/novice/01-02
	[HP.local] ➤ python3 call_bubbleSort.py
	[14, 21, 27, 41, 43, 45, 46, 57, 70]
	
2. heap_sort.py -> implementasi dari Algoritma Heap Sort
	- call_heapSort.py -> cara menggunakan module heap_sort.py
	```python
	import heap_sort
	
	random_list_of_nums = [35, 12, 43, 8, 51]
	heap_sort.heap_sort(random_list_of_nums)
	```
	
	```
	Output :
	[2019-12-04 22:07.58]  /drives/c/Users/HP/Documents/praxis-academy/novice/01-02
	[HP.local] ➤ python3 call_heapSort.py
	[8, 12, 35, 43, 51]

	
3. insertion_sort.py -> implementasi dari Algoritma Insertion Sort
	- call_insertionSort.py -> cara menggunakan module insertion_sort.py
	```python
	import insertion_sort

	random_list_of_nums = [9, 1, 15, 28, 6, 123, 33]
	insertion_sort.insertion_sort(random_list_of_nums)
	```
	
	```
	Output :
	[2019-12-04 22:11.16]  /drives/c/Users/HP/Documents/praxis-academy/novice/01-02
	[HP.local] ➤ python3 call_insertionSort.py
	[1, 6, 9, 15, 28, 33, 123]

	
4. quick_sort.py -> implementasi dari Algoritma Quick Sort
	- call_quickSort.py -> cara menggunakan module quick_sort.py
	```python
	import quick_sort

	random_list_of_nums = [22, 5, 1, 18, 99, 123, 68]
	quick_sort.quick_sort(random_list_of_nums)
	```
	
	```
	Output :
	[2019-12-04 22:13.19]  /drives/c/Users/HP/Documents/praxis-academy/novice/01-02
	[HP.local] ➤ python3 call_quickSort.py
	[1, 5, 18, 22, 68, 99, 123]

	
5. selection_sort.py -> implementasi dari Algoritma Selection Sort
	- call_selectionSort.py -> cara menggunakan module selection_sort.py
	```python
	import selection_sort

	random_list_of_nums = [12, 8, 3, 20, 11, -3, 77]
	selection_sort.selection_sort(random_list_of_nums)
	```
	
	```
	Output :
	[2019-12-04 22:13.21]  /drives/c/Users/HP/Documents/praxis-academy/novice/01-02
	[HP.local] ➤ python3 call_selectionSort.py
	[-3, 3, 8, 11, 12, 20, 77]
