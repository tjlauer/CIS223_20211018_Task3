# Results Table - Thomas Lauer (October 13, 2021)
<hr>

## Insertion Sort

<table style="width:100%">
  <tr>
    <th>Sorting Algorithm</th>
    <th>Case</th>
    <th>Reading</th>
    <th>10,000</th>
    <th>Avg</th>
    <th>100,000</th>
    <th>Avg</th>
    <th>1,000,000</th>
    <th>Avg</th>
  </tr>
  
  <tr>
    <td rowspan=6>Insertion Sort</td>
    <td rowspan=3>A</td>
    <td>1</td>
    <td>0.0019623</td>
    <td rowspan=3>0.0020202</td>
    <td>0.0203851</td>
    <td rowspan=3>0.0350398</td>
    <td>0.2495683</td>
    <td rowspan=3>0.2213227</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.0018398</td>
    <td>0.0251253</td>
    <td>0.2133161</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0.0022586</td>
    <td>0.0596089</td>
    <td>0.2010837</td>
  </tr>
  
  <tr>
    <td rowspan=3>B</td>
    <td>1</td>
    <td>8.9239341</td>
    <td rowspan=3>9.2707758</td>
    <td>650.3298678</td>
    <td rowspan=3>652.0324660</td>
    <td>57333.7344588</td>
    <td rowspan=3>57414.1580672</td>
  </tr>
  <tr>
    <td>2</td>
    <td>9.22562</td>
    <td>650.5975474</td>
    <td>57433.2350814</td>
  </tr>
  <tr>
    <td>3</td>
    <td>9.6627733</td>
    <td>655.1699829</td>
    <td>57475.5046613</td>
  </tr>
</table>

Insertion Sort - Case A => O(n)<br>
Insertion Sort - Case B => O(n^2)<br>

![InjectionSort_CaseA_Timings](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/InsertionSort_CaseA.svg?raw=true)
![InjectionSort_CaseB_Timings](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/InsertionSort_CaseB.svg?raw=true)
![InjectionSort_Durations](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/InsertionSort_Durations.svg?raw=true)

<br><hr>

## Merge Sort

<table style="width:100%">
  <tr>
    <th>Sorting Algorithm</th>
    <th>Case</th>
    <th>Reading</th>
    <th>10,000</th>
    <th>Avg</th>
    <th>100,000</th>
    <th>Avg</th>
    <th>1,000,000</th>
    <th>Avg</th>
  </tr>
  
  <tr>
    <td rowspan=6>Merge Sort</td>
    <td rowspan=3>A</td>
    <td>1</td>
    <td>0.0330934</td>
    <td rowspan=3>0.0316556</td>
    <td>0.4582884</td>
    <td rowspan=3>0.5920446</td>
    <td>5.0608495</td>
    <td rowspan=3>5.3586865</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.0309500</td>
    <td>0.582503</td>
    <td>5.3169194</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0.0309233</td>
    <td>0.7353425</td>
    <td>5.6982906</td>
  </tr>
  
  <tr>
    <td rowspan=3>B</td>
    <td>1</td>
    <td>0.0340661</td>
    <td rowspan=3>0.0473675</td>
    <td>0.9141803</td>
    <td rowspan=3>0.7511805</td>
    <td>5.0180289</td>
    <td rowspan=3>4.9778625</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.0502247</td>
    <td>0.4729961</td>
    <td>4.9788671</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0.0578117</td>
    <td>0.8663651</td>
    <td>4.9366916</td>
  </tr>
</table>

Merge Sort - Case A => O(n)<br>
Merge Sort - Case B => O(n)<br>

![MergeSort_CaseA_Timings](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/MergeSort_CaseA.svg?raw=true)
![MergeSort_CaseB_Timings](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/MergeSort_CaseB.svg?raw=true)
![MergeSort_Durations](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/MergeSort_Durations.svg?raw=true)

<br><hr>

## Counting Sort

<table style="width:100%">
  <tr>
    <th>Sorting Algorithm</th>
    <th>Case</th>
    <th>Reading</th>
    <th>10,000</th>
    <th>Avg</th>
    <th>100,000</th>
    <th>Avg</th>
    <th>1,000,000</th>
    <th>Avg</th>
  </tr>
  
  <tr>
    <td rowspan=6>Counting Sort</td>
    <td rowspan=3>A</td>
    <td>1</td>
    <td>0.0064525</td>
    <td rowspan=3>0.0077320</td>
    <td>0.0923856</td>
    <td rowspan=3>0.1171897</td>
    <td>0.8215346</td>
    <td rowspan=3>1.0777135</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.0095489</td>
    <td>0.0761710</td>
    <td>0.8353502</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0.0071946</td>
    <td>0.1830124</td>
    <td>1.5762558</td>
  </tr>
  
  <tr>
    <td rowspan=3>B</td>
    <td>1</td>
    <td>0.0070597</td>
    <td rowspan=3>0.0084587</td>
    <td>0.1669267</td>
    <td rowspan=3>0.1481636</td>
    <td>0.8373364</td>
    <td rowspan=3>0.8764878</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.0095054</td>
    <td>0.1032503</td>
    <td>0.9788574</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0.0088111</td>
    <td>0.1743139</td>
    <td>0.8132695</td>
  </tr>
  
</table>

Counting Sort - Case A => O(n)<br>
Counting Sort - Case B => O(n)<br>

![CountingSort_CaseA_Timings](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/CountingSort_CaseA.svg?raw=true)
![CountingSort_CaseB_Timings](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/CountingSort_CaseB.svg?raw=true)
![CountingSort_Durations](https://github.com/tjlauer/CIS223_Task3/blob/main/Images/CountingSort_Durations.svg?raw=true)
