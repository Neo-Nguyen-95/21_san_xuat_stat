## bài 2 tập hợp và các phép toán trên tập hợp

## thuật ngữ

- tập hợp, tập con, tập hợp bằng nhau, tập rỗng
- hợp, giao, hiệu của hai tập hợp, phần bù của một tập con
- biểu đồ ven


## kiến thức, kỹ năng

- nhận biết các khái niệm cơ bản về tập hợp.
- thực hiện các phép toán trên tập hợp và vận dụng giải một số bài toán có nội dung thực tiễn.
- sử dụng biểu đồ ven để biểu diễn tập hợp và các phép toán trên tập hợp.

câu lạc bộ lịch sử có 12 thành viên (không có hai bạn nào trùng tên), tổ chức hai chuyên đề trên một phần mềm họp trực tuyến. tên các thành viên tham gia mỗi chuyên đề được hiển thị trên màn hình (h. 1.1).


bài học này sẽ giúp em trả lời câu hỏi trên bằng kiến thức cơ bản về tập hợp và các phép toán trên tập hợp.

## 1. các khái niệm cơ bản về tập hợp

## a. tập hợp

1】 ho1. trong tình huống trên, gọi $a$ là tập hợp những thành viên tham gia chuyên đề $1, b$ là tập hợp những thành viên tham gia chuyên đề 2 .
a) nam có là một phần tử của tập hợp $a$ không? ngân có là một phần tử của tập hợp $b$ không?
b) hãy mô tả các tập hợp $a$ và $b$ bằng cách liệt kê các phần tử.

hd2. cho tập hợp:
c = \{châu á; châu âu; châu đại dương; châu mĩ; châu nam cực; châu phi\}.
a) hãy chỉ ra tính chất đặc trưng cho các phần tử của tập hợp $c$.
b) tập hợp $c$ có bao nhiêu phần tử?

có thể mô tả một tập hợp bằng một trong hai cách sau:
cách 1. liệt kê các phần tử của tập hợp;
cách 2. chỉ ra tính chất đặc trưng cho các phần tử của tập hợp.
$a \in s$ : phần tử $a$ thuộc tập hợp $s$.
$a \notin s$ : phần tử $a$ không thuộc tập hợp $s$.

ví dụ 1. cho $d=\{n \in \mathbb{n} \mid n$ là số nguyên tố, $5<n<20\}$.
a) dùng kí hiệu $\in, \notin$ để viết câu trả lời cho câu hỏi sau: trong các số $5 ; 12 ; 17 ; 18$, số nào thuộc tập $d$, số nào không thuộc tập $d$ ?
b) viết tập hợp $d$ bằng cách liệt kê các phần tử. tập hợp $d$ có bao nhiêu phần tử?

## giải

a) $5 \notin d ; 12 \notin d ; 17 \in d ; 18 \notin d$.
b) $d=\{7 ; 11 ; 13 ; 17 ; 19\}$. tập hợp $d$ có 5 phần tử.

chú ý. số phần tử của tập hợp $s$ được kí hiệu là $n(s)$. chẳng hạn, tập hợp $a$ trong $\mathrm{h} đ 1$ có số phần tử là 7 , ta viết $n(a)=7$.

số nào thuộc tập nghiệm của phương trình $x^{2}+1=0$ ?

không có số nào vì phương trình vô nghiệm!


tập hợp không chứa phần tử nào được gọi là tập rỗng, kí hiệu là $\varnothing$.

chẳng hạn:

- tập hợp các nghiệm của phương trình $x^{2}+1=0$ là tập rỗng;
- tập hợp những người sống trên mặt trời là tập rỗng.

1> luyện tập 1. gọi $x$ là tập nghiệm của phương trình

$$
x^{2}-24 x+143=0
$$

các mệnh đề sau đúng hay sai?
a) $13 \in x$;
b) $11 \notin x$;
c) $n(x)=2$.

## b. tập hợp con

н03. gọi $h$ là tập hợp các bạn tham gia chuyên đề 2 trong tình huống mở đầu có tên bắt đầu bằng chữ h . các phần tử của tập hợp h có là phần tử của tập hợp $b$ trong hd 1 không?

nếu mọi phần tử của tập hợp $t$ đều là phần tử của tập hợp $s$ thì ta nói $t$ là một tập hợp con (tập con) của $s$ và viết là $t \subset s$ (đọc là $t$ chứa trong $s$ hoặc $t$ là tập con của $s$ ).

- thay cho $t \subset s$, ta còn viết $s \supset t$ (đọc là $s$ chứa $t$ ).
- kí hiệu $t \not \subset s$ để chỉ $t$ không là tập con của $s$.


## nhận xét

- từ định nghĩa trên, $t$ là tập con của $s$ nếu mệnh đề sau đúng:

$$
\forall x, x \in t \rightarrow x \in s .
$$

- quy ước tập rỗng là tập con của mọi tập hợp.

người ta thường minh hoạ một tập hợp bằng một hình phẳng được bao quanh bởi một đường kín, gọi


hinh 1.2 là biểu đồ ven (h.1.2).

minh hoạ $t$ là một tập con của $s$ như hình 1.3.
】 ví dụ 2. cho tập hợp $s=\{2 ; 3 ; 5\}$. những tập hợp nào sau đây là tập con của $s$ ?

$$
s_{1}=\{3\} ; \quad s_{2}=\{0 ; 2\} ; \quad s_{3}=\{3 ; 5\} .
$$



hinh 1.3

## giải

các tập hợp $s_{1}=\{3\}, s_{3}=\{3 ; 5\}$ là những tập con của $s(h .1 .4)$.


## c. hai tập hợp bằng nhau

н04. sơn và thu viết tập hợp các số chính phương nhỏ hơn 100 như sau:
son: $s=\{0 ; 1 ; 4 ; 9 ; 16 ; 25 ; 36 ; 49 ; 64 ; 81\}$;
thu: $t=\{n \in \mathbb{n} \mid n$ là số chính phương; $n<100\}$.
hỏi bạn nào viết đúng?

hai tập hợp $s$ và $t$ được gọi là hai tập hợp bằng nhau nếu mỗi phần tử của $t$ cũng là phần tử của tập hợp $s$ và ngược lại. kí hiệu là $s=t$.

ví dụ 3. cho hai tập hợp:
$c=\{n \in \mathbb{n} \mid n$ là bội chung của 2 và $3 ; n<30\}$;
$d=\{n \in \mathbb{n} \mid n$ là bội của 6; $n<30\}$.

```
nếu s c t và t c s
thi s = t.
```



chứng minh $c=d$.

## giải

ta có: $c=\{0 ; 6 ; 12 ; 18 ; 24\}$;

$$
d=\{0 ; 6 ; 12 ; 18 ; 24\} .
$$

vậy $c=d$.
) luyện tập 2. giả sử $c$ là tập hợp các hình bình hành có hai đường chéo vuông góc; $d$ là tập hợp các hình vuông.

các mệnh đề sau đúng hay sai?
a) $c \subset d$;
b) $c \supset d$;
c) $c=d$.

## 2. các tập hợp số

## a. mối quan hệ giữa các tập hợp số

- tập hợp các số tự nhiên $\mathbb{n}=\{0 ; 1 ; 2 ; 3 ; 4 ; \ldots\}$.
- tập hợp các số nguyên $\mathbb{z}$ gồm các số tự nhiên và các số nguyên âm:

$$
\mathbb{z}=\{\ldots ;-3 ;-2 ;-1 ; 0 ; 1 ; 2 ; 3 ; \ldots\}
$$

- tập hợp các số hữu tỉ $\mathbb{q}$ gồm các số viết được dưới dạng phân số $\frac{a}{b}$, với $a, b \in \mathbb{z}, b \neq 0$. số hữu tỉ còn được biểu diễn dưới dạng số thập phân hữu hạn hoặc vô hạn tuần hoàn.
- tập hợp các số thực $\mathbb{r}$ gồm các số hữu tỉ và các số vô tỉ. số vô tỉ là các số thập phân vô hạn không tuần hoàn.

1】 ho5. các mệnh đề sau đúng hay sai?
a) mọi số nguyên đều viết được dưới dạng phân số;
b) tập hợp các số thực chứa tập hợp các số hữu tỉ;
c) tồn tại một số thực không là số hữu tỉ.

mối quan hệ giữa các tập hợp số: $\mathbb{n} \subset \mathbb{z} \subset \mathbb{q} \subset \mathbb{r}$.


hinh 1.5

ví dụ 4. hãy xác định tính đúng sai của các mệnh đề sau:
a) $3,274 \in \mathbb{q}$;
b) $\sqrt{2} \in \mathbb{r}$;
c) $\frac{3}{4} \in \mathbb{z}$.

## giải

a) $3,274 \in \mathbb{q}$ là mệnh đề đúng.
b) $\sqrt{2} \in \mathbb{r}$ là mệnh đề đúng.
c) $\frac{3}{4} \in \mathbb{z}$ là mệnh đề sai.

8】 luyện tập 3. cho tập hợp $c=\{-4 ; 0 ; 1 ; 2\}$. các mệnh đề sau đúng hay sai?
a) $c$ là tập con của $\mathbb{z}$;
b) $c$ là tập con của $\mathbb{n}$;
c) $c$ là tập con của $\mathbb{r}$.

## b. các tệp con thường dùng của $\mathbb{r}$

hd6. cho hai tập hợp $c=\{x \in \mathbb{r} \mid x \geq 3\}$ và $d=\{x \in \mathbb{r} \mid x>3\}$.
các mệnh đề sau đúng hay sai?
a) $c, d$ là các tập con của $\mathbb{r}$;
b) $\forall x, x \in c \rightarrow x \in d$;
c) $3 \in c$ nhưng $3 \notin d$;
d) $c=d$.

một số tập con thường dùng của tập số thực $\mathbb{r}$ :

- khoảng

- đoạn
$[a ; b]=\{x \in \mathbb{r} \mid a \leq x \leq b\}$
- nửa khoảng


kí hiệu $+\infty$ : đọc là dương vô cực (hoặc dương vô cùng).
kí hiệu $-\infty$ : đọc là âm vô cực (hoặc âm vô cùng).
$a, b$ gọi là các đầu mút của đoạn, khoảng hay nửa khoảng.

ví dụ 5. viết các tập hợp sau dưới dạng các khoảng, đoạn, nửa khoảng trong $\mathbb{r}$ rồi biểu diễn trên trục số: $c=\{x \in \mathbb{r} \mid 2 \leq x \leq 7\} ; \quad d=\{x \in \mathbb{r} \mid x<2\}$.

## giải

$c=[2 ; 7]$
$d=(-\infty ; 2)$


| 1) $x \in[2 ; 5]$ |
| :--- |
| 2) $x \in(2 ; 5]$ |
| 3) $x \in[7 ;+\infty)$ |
| 4) $x \in(7 ; 10)$ |

a) $2<x \leq 5$
b) $x \geq 7$
c) $7<x<10$
d) $2 \leq x \leq 5$
e) $2 \leq x<5$

## 3. các phép toán trên tập hợp

## a. giao của hai tập hợp

hoz. viết tập hợp $x$ gồm những thành viên tham gia cả hai chuyên đề 1 và 2 trong tình huống mở đầu.
tập $x$ có phải là tập con của tập $a$ không? tập $x$ có phải là tập con của tập $b$ không? ( $a, b$ là các tập hợp trong hd 1 ).

tập hợp gồm các phần tử thuộc cả hai tập hợp $s$ và $t$ gọi là giao của hai tập hợp $s$ và $t$, kí hiệu là $s \cap t$.

$$
s \cap t=\{x \mid x \in s \text { và } x \in t\} .
$$



hinh 1.6

## ví dụ 6

a) cho hai tập hợp $c=\{4 ; 7 ; 27\}$ và $d=\{2 ; 4 ; 9 ; 27 ; 36\}$. hãy xác định tập hợp $c \cap d$.
b) cho hai tập hợp $e=[1 ;+\infty)$ và $f=(-\infty ; 3]$. hãy xác định tập hợp $e \cap f$.

## giải

a) giao của hai tập hợp $c$ và $d$ là $c \cap d=\{4 ; 27\}$.
b) giao của hai tập hợp $e$ và $f$ là $e \cap f=[1 ; 3]$.


】 luyện tập 5. cho các tập hợp $c=[1 ; 5], d=[-2 ; 3]$. hãy xác định tập hợp $c \cap d$.

## b. hợp của hai tập hợp

нo8. trở lại tình huống mở đầu, hãy xác định tập hợp các thành viên tham gia chuyên đề 1 hoặc chuyên đề 2.

tập hợp gồm các phần tử thuộc tập hợp $s$ hoặc thuộc tập hợp $t$ gọi là hợp của hai tập hợp $s$ và $t$, kí hiệu là $s \cup t$.

$$
s \cup t=\{x \mid x \in s \text { hoăc } x \in t\} .
$$

ví dụ 7. cho hai tập hợp: $c=\{2 ; 3 ; 4 ; 7\} ; d=\{-1 ; 2 ; 3 ; 4 ; 6\}$.
hãy xác định tập hợp $c \cup d$.

## giải

hợp của hai tập hợp $c$ và $d$ là $c \cup d=\{-1 ; 2 ; 3 ; 4 ; 6 ; 7\}$.

hinh 1.8


hinh 1.8

ví dụ 8. trở lại câu hỏi trong tình huống mở đầu. gọi $a$ là tập hợp những thành viên tham gia chuyên đề $1, b$ là tập hợp những thành viên tham gia chuyên đề 2 .

ta có: $a \cup b=\{$ nam; hương; chi; tú; bình; ngân; khánh; hiện; hiền; lam\}.
tập $a \cup b$ có 10 phần tử, tức là có 10 thành viên tham gia một hoặc hai chuyên đề.
số thành viên vắng mặt trong cả hai chuyên đề là:

$$
12 \text { - } 10 \text { = } 2 \text { (thành viên). }
$$

luyện tập 6. hãy biểu diễn tập hợp $a \cup b$ bằng biểu đồ ven, với $a, b$ được cho trong hd 1 .

## c. hiệu của hai tập hợp

но9. trở lại tình huống mở đầu, hãy xác định tập hợp các thành viên chỉ tham gia chuyên đề 1 mà không tham gia chuyên đề 2 .

- hiệu của hai tập hợp $s$ và $t$ là tập hợp gồm các phần tử thuộc $s$ nhưng không thuộc $t$, kí hiệu là $s \backslash t$.
$s \backslash t=\{x \mid x \in s$ và $x \notin t\}$.
- nếu $t \subset s$ thì $s \backslash t$ được gọi là phần bù của $t$ trong $s$, kí hiệu là $c_{s} t$.

chú ý. $c_{s} s=\varnothing$.


hinh 1.9


hinh 1.10

ví dụ 9. cho các tập hợp: $d=\{-2 ; 3 ; 5 ; 6\} ; e=\{x \mid x$ là số nguyên tố nhỏ hơn 10\}; $x=\{x \mid x$ là số nguyên dương nhỏ hơn 10$\}$.
a) tìm $d \backslash e$ và $e \backslash d$.
b) $e$ có là tập con của $x$ không? hãy tìm phần bù của $e$ trong $x$ (nếu có).

## giải

a) ta có: $e=\{2 ; 3 ; 5 ; 7\}$.

do đó, $d \backslash e=\{-2 ; 6\} ; e \backslash d=\{2 ; 7\}$.
b) ta có: $x=\{1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9\}$. vậy $e$ là tập con của $x$.

phần bù của $e$ trong $x$ là $x \backslash e=c_{x} e=\{1 ; 4 ; 6 ; 8 ; 9\}$.
) luyện tập 7. tìm phần bù của các tập hợp sau trong $\mathbb{r}$ :
a) $(-\infty ;-2)$;
b) $[-5 ;+\infty)$.

vận dụng. lớp 10a có 24 bạn tham gia thi đấu bóng đá và cầu lông, trong đó có 16 bạn thi đấu bóng đá và 11 bạn thi đấu cầu lông. giả sử các trận bóng đá và cầu lông không tổ chức đồng thời. hỏi có bao nhiêu bạn lớp 10 a tham gia thi đấu cả bóng đá và cầu lông?
gợi ý. gọi x là số bạn tham gia thi đấu cả bóng đá và cầu lông.


ta có: $n(a \cup b)=n(a)+n(b)-n(a \cap b)$.