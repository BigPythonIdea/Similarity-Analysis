# Similarity-Analysis

### 問題:相似度分析
#### 主要公式: ||v1||dot||v2||cos()

對比問題 比如說 


V1 = 'apple' 'banana' 'blue'


v2 = 'Red' 'cat' 'dog'


v1 = [1,2,3]


v2 = [1,2,3]


=> 100%

解決方案:建立字典法


將2文本合成一個字典，再分別進入字典比對是否有該單詞若有就將標籤+1加到list中

測試結果:

【01text】
```
Abbott has been identified as a potentially responsible party for investigation and cleanup costs at a number of locations in the United States and Puerto Rico under federal and state remediation laws and is investigating potential contamination at a number of company-owned locations.  Abbott has recorded an estimated cleanup cost for each site for which management believes Abbott has a probable loss exposure.  No individual site cleanup exposure is expected to exceed $3 million, and the aggregate cleanup exposure is not expected to exceed $15 million.

 

There are a number of patent disputes with third parties who claim Abbott’s products infringe their patents.  In April 2007, New York University (NYU) and Centocor, Inc. filed a lawsuit in the Eastern District of Texas asserting that HUMIRA infringes a patent co-owned by NYU and Centocor.  In June 2009, a jury found that Abbott had willfully infringed the patent and awarded NYU and Centocor approximately $1.67 billion in past compensatory damages.  The award is subject to review by the trial court.  Abbott will ask the trial court to overturn the verdict and/or reduce the damages award.  In the event that the trial court does not overturn the verdict, Abbott will appeal.  Abbott is confident in the merits of its case and believes that it will prevail on appeal.  As a result, no reserves have been recorded in this case.  Abbott’s acquisition of Kos Pharmaceuticals Inc. resulted in the assumption of various cases and investigations and Abbott has recorded reserves related to several of those cases and investigations.

 

There are several civil actions pending brought by individuals or entities that allege generally that Abbott and numerous pharmaceutical companies reported false or misleading pricing information relating to the average wholesale price of certain pharmaceutical products in connection with federal, state and private reimbursement.  Civil actions have also been brought against Abbott, and in some cases other members of the pharmaceutical industry, by state attorneys general seeking to recover alleged damages on behalf of state Medicaid programs.  In May 2006, Abbott was notified that the U.S. Department of Justice intervened in a civil whistle-blower lawsuit alleging that Abbott inflated prices for Medicaid and Medicare reimbursable drugs.  Abbott has settled a few of the cases and recorded reserves for its estimated losses in a few other cases, however, Abbott is unable to estimate the range or amount of possible loss for the remaining cases, and no loss reserves have been recorded for them.  Many of the products involved in these cases are Hospira products.  Hospira, Abbott’s former hospital products business, was spun off to Abbott’s shareholders in 2004.  Abbott retained liability for losses that result from these cases and investigations to the extent any such losses both relate to the sale of Hospira’s products prior to the spin-off of Hospira and relate to allegations that were made in such pending and future cases and investigations that were the same as allegations existing at the date of the spin-off.

 

There are several civil actions pending brought by state attorneys general and private entities alleging antitrust and unfair competition claims in connection with the sales of TriCor. Abbott licenses TriCor from a third party and the licensor has also been named as a defendant.  Settlements have been reached in all of these cases except the state attorneys general, however, Abbott is unable to estimate a reserve and no loss reserve has been recorded for the remaining TriCor cases.

 

Within the next year, legal proceedings may occur that may result in a change in the estimated reserves recorded by Abbott.  For its legal proceedings and environmental exposures, except as noted above, Abbott estimates the range of possible loss to be from approximately $205 million to $415 million.  The recorded reserve balance at June 30, 2009 for these proceedings and exposures was approximately $275 million.  These reserves represent management’s best estimate of probable loss, as defined by Statement of Financial Accounting Standards No. 5 “Accounting for Contingencies.”

 

While it is not feasible to predict the outcome of all such proceedings and exposures with certainty, management believes that their ultimate disposition should not have a material adverse effect on Abbott’s financial position, cash flows, or results of operations, except for the cases and investigations discussed in the third paragraph and the patent case discussed in the second paragraph of this footnote, the resolution of which could be material to cash flows or results of operations.
```


【02text】

```
Abbott has been identified as a potentially responsible party for investigation and cleanup costs at a number of locations in the United States and Puerto Rico under federal and state remediation laws and is investigating potential contamination at a number of company-owned locations.  Abbott has recorded an estimated cleanup cost for each site for which management believes Abbott has a probable loss exposure.  No individual site cleanup exposure is expected to exceed $3 million, and the aggregate cleanup exposure is not expected to exceed $15 million.

 

There are a number of patent disputes with third parties who claim Abbott’s products infringe their patents.  In April 2007, New York University (NYU) and Centocor, Inc. filed a lawsuit in the Eastern District of Texas asserting that HUMIRA infringes a patent co-owned by NYU and Centocor and exclusively licensed to Centocor.  In June 2009, a jury found that Abbott had willfully infringed the patent and awarded NYU and Centocor approximately $1.67 billion in past compensatory damages.  In October 2009, the district court overturned the jury’s finding that Abbott’s infringement was willful, but denied Abbott’s request to overturn the jury’s verdict on validity, infringement, and damages.  Abbott will appeal the jury’s verdict.  Abbott is confident in the merits of its case and believes that it will prevail on appeal.  As a result, no reserves have been recorded in this case.  Abbott’s acquisition of Kos Pharmaceuticals Inc. resulted in the assumption of various cases and investigations and Abbott has recorded a reserve.

 

There are several civil actions pending brought by individuals or entities that allege generally that Abbott and numerous pharmaceutical companies reported false or misleading pricing information relating to the average wholesale price of certain pharmaceutical products in connection with federal, state and private reimbursement.  Civil actions have also been brought against Abbott, and in some cases other members of the pharmaceutical industry, by state attorneys general seeking to recover alleged damages on behalf of state Medicaid programs.  In May 2006, Abbott was notified that the U.S. Department of Justice intervened in a civil whistle-blower lawsuit alleging that Abbott inflated prices for Medicaid and Medicare reimbursable drugs.  Abbott has settled a few of the cases and recorded reserves for its estimated losses in a few other cases, however, Abbott is unable to estimate the range or amount of possible loss for the remaining cases, and no loss reserves have been recorded for them.  Many of the products involved in these cases are Hospira products.  Hospira, Abbott’s former hospital products business, was spun off to Abbott’s shareholders in 2004.  Abbott retained liability for losses that result from these cases and investigations to the extent any such losses both relate to the sale of Hospira’s products prior to the spin-off of Hospira and relate to allegations that were made in such pending and future cases and investigations that were the same as allegations existing at the date of the spin-off.

 

Within the next year, legal proceedings may occur that may result in a change in the estimated reserves recorded by Abbott.  For its legal proceedings and environmental exposures, except as noted above, Abbott estimates the range of possible loss to be from approximately $230 million to $385 million.  The recorded reserve balance at September 30, 2009 for these proceedings and exposures was approximately $285 million.  These reserves represent management’s best estimate of probable loss, as defined by FASB Accounting Standards Codification No. 450, “Contingencies.”

 

While it is not feasible to predict the outcome of all such proceedings and exposures with certainty, management believes that their ultimate disposition should not have a material adverse effect on Abbott’s financial position, cash flows, or results of operations, except for the cases and investigations discussed in the third paragraph and the patent case discussed in the second paragraph of this footnote, the resolution of which could be material to cash flows or results of operations.

 

In the third quarter 2009, Abbott and Medtronic, Inc. reached a settlement resolving all outstanding intellectual property litigation between the two parties.  Under the terms of the settlement, Medtronic paid Abbott $400 million.  The settlement also includes a mutual agreement not to pursue additional litigation on current and future vascular products, subject to specific conditions and time limits.  In connection with the settlement, Abbott recognized a gain of $287 million which is included in Other (income) expense, net.  The remaining amounts will be recognized as royalty income as earned.
```

### My version: 0.7253308882729255
