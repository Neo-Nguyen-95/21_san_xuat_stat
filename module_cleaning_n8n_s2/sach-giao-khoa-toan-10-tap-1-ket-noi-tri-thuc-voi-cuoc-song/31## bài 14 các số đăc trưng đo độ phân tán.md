## bài 14 các số đăc trưng đo độ phân tán

## thuật ngữ

- khoảng biến thiên
- khoảng tứ phân vị
- phương sai
- độ lệch chuẩn


## kiến thức, kĩ năng

- tính các số đặc trưng đo độ phân tán.
- biết ý nghĩa của các số đặc trưng đo độ phân tán.
- phát hiện các giá trị bất thường sử dụng các công cụ toán học.

dưới đây là điểm trung bình môn học kì i của hai bạn an và bình:

|  | toán | vật lí | hoá học | ngữ văn | lịch sử | địa lí | tin học | tiếng anh |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| an | 9,2 | 8,7 | 9,5 | 6,8 | 8,0 | 8,0 | 7,3 | 6,5 |
| bình | 8,2 | 8,1 | 8,0 | 7,8 | 8,3 | 7,9 | 7,6 | 8,1 |

điểm trung bình môn học kì của an và bình đều là 8,0 nhưng rõ ràng bình "học đều" hơn an. có thể dùng những số đặc trưng nào để đo mức độ "học đều"?
bài này sẽ giới thiệu một vài số đặc trưng như vậy.

## 1. khoảng biến thiên và khoảng tứ phân vị

hd1. một cổ động viên của câu lạc bộ everton, anh đã thống kê điểm số mà hai câu lạc bộ leicester city và everton đạt được trong năm mùa giải ngoại hạng anh gần đây, từ mùa giải 2014-2015 đến mùa giải 2018-2019 như sau:

| leicester city: | 41 | 81 | 44 | 47 | 52. |
| :--- | ---: | :--- | :--- | :--- | :--- |
| everton: | 47 | 47 | 61 | 49 | 54. |

cổ động viên đó cho rằng, everton thi đấu ổn định hơn leicester city. em có đồng ý với nhận định này không? vì sao?
trong 5 mùa giải, điểm thấp nhất, cao nhất của leicester city lần lượt là 41; 81 trong khi của everton là 47; 61. về trực quan, thành tích của everton ổn định hơn leicester city. người ta có nhiều cách để đo sự ổn định này. cách đơn giản nhất là dùng hiệu số (điểm cao nhất điểm thấp nhất). giá trị này được gọi là khoảng biến thiên.
khoảng biến thiên, kí hiệu là $r$, là hiệu số giữa giá trị lớn nhất và giá trị nhỏ nhất trong mẫu số liệu.

[^0]ví dụ 1. điểm kiểm tra học kì môn toán của các bạn tổ 1, tổ 2 lớp 10a được cho như sau:

| tồ 1: | 7 | 8 | 8 | 9 | 8 | 8 | 8. |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| tổ 2: | 10 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8. |

a）điểm kiểm tra trung bình của hai tổ có như nhau không？
b）tính các khoảng biến thiên của hai mẫu số liệu．căn cứ trên chỉ số này，các bạn tổ nào học đồng đều hơn？

## giải

a）điểm kiểm tra trung bình của hai tổ đều bằng 8 ．
b）đối với tổ 1：điểm kiểm tra thấp nhất，cao nhất tương ưng là 7；9．do đó khoảng biến thiên là：$r_{1}=9-7=2$ ．
đối với tổ 2：điểm kiểm tra thấp nhất，cao nhất tương ứng là 6；10．do đó khoảng biến thiên là：$r_{2}=10-6=4$ ．
do $r_{2}>r_{1}$ nên ta nói các bạn tổ 1 học đều hơn các bạn tổ 2 ．
》】 luyện tập 1．mẫu số liệu sau cho biết chiều cao（đơn vị cm）của các bạn trong tổ：

$$
\begin{array}{llllllll}
163 & 159 & 172 & 167 & 165 & 168 & 170 & 161 .
\end{array}
$$

tính khoảng biến thiên của mẫu số liệu này．
nhận xét．sử dụng khoảng biến thiên có ưu điểm là đơn giản，dễ tính toán song khoảng biến thiên chỉ sử dụng thông tin của giá trị lớn nhất và giá trị nhỏ nhất mà bỏ qua thông tin từ tất cả các giá trị khác．do đó，khoảng biến thiên rất dễ bị ảnh hưởng bởi các giá trị bất thường．
1】 h02．trong một tuần，nhiệt độ cao nhất trong ngày（đơn vị ${ }^{\circ} \mathrm{c}$ ）tại hai thành phố hà nội và điện biên được cho như sau：

| hà nội： | 23 | 25 | 28 | 28 | 32 | 33 | 35. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| điện biên： | 16 | 24 | 26 | 26 | 26 | 27 | 28. |

a）tính các khoảng biến thiên của mỗi mẫu số liệu và so sánh．
b）em có nhận xét gì về sự ảnh hưởng của giá trị 16 đến khoảng biến thiên của mẫu số liệu về nhiệt độ cao nhất trong ngày tại điện biên？
c）tính các tứ phân vị và hiệu $q_{3}-q_{1}$ cho mỗi mẫu số liệu．có thể dùng hiệu này để đo độ phân tán của mẫu số liệu không？

khoảng tứ phân vị，kí hiệu là $\delta_{q}$ ，là hiệu số giữa tứ phân vị thứ ba và tứ phân vị thứ nhất，tức là：

$$
\delta_{q}=q_{3}-q_{1}
$$

về bản chất，khoảng tứ phân vị là khoảng biến thiên của $50 \%$ số liệu chính giữa của mẫu số liệu đã sắp xểp．

ý nghĩa．khoảng tứ phân vị cũng là một số đo độ phân tán của mẫu số liệu．khoảng tứ phân vị càng lớn thì mẫu số liệu càng phân tán．
chú ý．một số tài liệu gọi khoảng biến thiên là biên độ và khoảng tứ phân vị là độ trải giữa．


vi dụ 2．mẫu số liệu sau cho biết số ghế trống tại một rạp chiếu phim trong 9 ngày：

$$
\begin{array}{lllllllll}
7 & 8 & 22 & 20 & 15 & 18 & 19 & 13 & 11 .
\end{array}
$$

tìm khoảng tứ phân vị cho mẫu số liệu này．

## giải

trước hết，ta sắp xếp mẫu số liệu theo thứ tự không giảm：

$$
\begin{array}{lllllllll}
7 & 8 & 11 & 13 & 15 & 18 & 19 & 20 & 22 .
\end{array}
$$

mẫu số liệu gồm 9 giá trị nên trung vị là số ở vị trí chính giữa $q_{2}=15$.
nửa số liệu bên trái là $7,8,11,13$ gồm 4 giá trị, hai phần tử chính giữa là 8,11 .
do đó, $q_{1}=(8+11): 2=9,5$.
nửa số liệu bên phải là $18,19,20,22$ gồm 4 giá trị, hai phần tử chính giữa là 19,20 .
do đó, $q_{3}=(19+20): 2=19,5$.
vậy khoảng tứ phân vị cho mẩu số liệu là $\delta_{q}=19,5-9,5=10$.
】 luyện tập 2. mẫu số liệu sau đây cho biết số bài hát ở mỗi album trong bộ sưu tập của an:

$$
\begin{array}{llllllllll}
12 & 7 & 10 & 9 & 12 & 9 & 10 & 11 & 10 & 14 .
\end{array}
$$

hãy tìm khoảng tứ phân vị cho mẫu số liệu này.

## 2. phương sai và độ lệch chuẩn

khoảng biến thiên chỉ sử dụng thông tin của giá trị lớn nhất và nhỏ nhất của mẫu số liệu (bỏ qua thông tin của tất cả các giá trị khác), còn khoảng tứ phân vị chỉ sử dụng thông tin của $50 \%$ số liệu chính giữa. có một vài số đặc trưng khác đo độ phân tán sử dụng thông tin của tất cả các giá trị trong mẫu số liệu. hai trong số đó là phương sai và độ lệch chuẩn.
cụ thể là với mẫu số liệu $x_{1}, x_{2}, \ldots, x_{n}$, nếu gọi số trung bình là $\bar{x}$ thì với mỗi giá trị $x_{i}$, độ lệch của nó so với giá trị trung bình là $x_{i}-\bar{x}$.

- phương sai là giá trị $s^{2}=\frac{\left(x_{1}-\bar{x}\right)^{2}+\left(x_{2}-\bar{x}\right)^{2}+\ldots+\left(x_{n}-\bar{x}\right)^{2}}{n}$.
- căn bậc hai của phương sai, $s=\sqrt{s^{2}}$, được gọi là độ lệch chuẩn.

chú ý. người ta còn sử dụng đại lượng để đo độ phân tán của mẫu số liệu:

$$
\hat{s}^{2}=\frac{\left(x_{1}-\bar{x}\right)^{2}+\left(x_{2}-\bar{x}\right)^{2}+\ldots+\left(x_{n}-\bar{x}\right)^{2}}{n-1}
$$

ý nghĩa. nếu số liệu càng phân tán thì phương sai và độ lệch chuẩn càng lớn.
vi dụ 3. mẫu số liệu sau đây cho biết sĩ số của 5 lớp khối 10 tại một trường trung học:

$$
\begin{array}{lllll}
43 & 45 & 46 & 41 & 40 .
\end{array}
$$

tìm phương sai và độ lệch chuẩn cho mẫu số liệu này.

## giải

số trung bình của mẫu số liệu là: $\bar{x}=\frac{43+45+46+41+40}{5}=43$.
ta có bảng sau:

| giá trị | độ lệch | bình phương độ lệch |
| :---: | :---: | :---: |
| 43 | $43-43=0$ | 0 |
| 45 | $45-43=2$ | 4 |
| 46 | $46-43=3$ | 9 |
| 41 | $41-43=-2$ | 4 |
| 40 | $40-43=-3$ | 9 |
| tồng |  | 26 |

bạn có thể sử dụng máy tính cầm tay, phần mềm bảng tính hay phần mềm thống kê để tính các số đặc trưng.

mẫu số liệu gồm 5 giá trị nên $n=5$. do đó phương sai là: $s^{2}=\frac{26}{5}=5,2$.
độ lệch chuẩn là: $s=\sqrt{5,2} \approx 2,28$.

1) luyện tập 3. düng đồng hồ đo thời gian có độ chia nhỏ nhất đến 0,001 giây để đo 7 lần thời gian rơi tự do của một vật bắt đầu từ điểm $a\left(v_{a}=0\right)$ đến điểm $b$. kết quả đo như sau:

$$
\begin{array}{lllllll}
0,398 & 0,399 & 0,408 & 0,410 & 0,406 & 0,405 & 0,402 .
\end{array}
$$

(theo bài tập vật li 10, nhà xuất bản giáo dục việt nam, 2018)
hãy tính phương sai và độ lệch chuẩn cho mẫu số liệu này. qua các đại lượng này, em có nhận xét gì về độ chính xác của phép đo trên?

## 3. phát hiện số liệu bất thường hoặc không chính xác bằng biểu đố hộp

trong mẫu số liệu thống kê, có khi gặp những giá trị quá lớn hoặc quá nhỏ so với đa số các giá trị khác. những giá trị này được gọi là giá trị bất thường. chúng xuất hiện trong mẫu số liệu có thể do nhầm lẫn hay sai sót nào đó. ta có thể dùng biểu đồ hộp để phát hiện những giá trị bất thường này.


hình 5.5. biểu đồ hộp
các giá trị lớn hơn $q_{3}+1,5 \cdot \delta_{q}$ hoặc bé hơn $q_{1}-1,5 \cdot \delta_{q}$ được xem là giá trị bất thường.
vi dụ 4. hàm lượng natri (đơn vị mg) trong 100 g một số loại ngũ cốc được cho như sau:

| 0 | 340 | 70 | 140 | 200 | 180 | 210 | 150 | 100 | 130 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 140 | 180 | 190 | 160 | 290 | 50 | 220 | 180 | 200 | 210. |

tìm giá trị bất thường trong mẫu số liệu trên bằng cách sử dụng biểu đồ hộp.

## giải

từ mẫu số liệu ta tính được $q_{1}=135$ và $q_{3}=205$. do đó, khoảng tứ phân vị là:

$$
\delta_{q}=205-135=70 .
$$

biểu đồ hộp cho mẫu số liệu này là:


ta có $q_{1}-1,5 \cdot \delta_{q}=30$ và $q_{3}+1,5 \cdot \delta_{q}=310$ nên trong mẫu số liệu có hai giá trị được xem là bất thường là 340 mg (lớn hơn 310 mg ) và 0 mg (bé hơn 30 mg ).
luyện tập 4. một mẫu số liệu có tứ phân vị thứ nhất là 56 và tứ phân vị thứ ba là 84 . hãy kiểm tra xem trong hai giá trị 10 và 100 giá trị nào được xem là giá trị bất thường.