# Numerical Solver Library 

The Numerical Solver Library (NSoL) is a Python-based open-source toolkit for research developed within the [GIFT-Surg][giftsurg] project and contains several implementations of denoising and deconvolution algorithms.
Please note that currently **only Python 2** is supported.

The algorithm and software were developed by [Michael Ebner][mebner] at the [Translational Imaging Group][tig] in the [Centre for Medical Image Computing][cmic] at [University College London (UCL)][ucl].

If you have any questions or comments (or find bugs), please drop an email to `michael.ebner.14@ucl.ac.uk`.

## Features

Implemented solvers include
* **Primal-Dual Methods** as described in [[Chambolle and Pock, 2010]](https://link.springer.com/article/10.1007/s10851-010-0251-1)
* **Alternating Direction Method of Multipliers (ADMM)** as described in, e.g., [[Diamond and Boyd, 2015]](http://stanford.edu/~boyd/papers/admm_distr_stats.html) 

to solve
* **L1- and L2-denoising** problems, i.e.
```math
\vec{x}^*:=\text{argmin}_{\vec{x}} \Big[\Vert \vec{x} - \vec{x}_0 \Vert_{\ell^p}^p + \alpha\,\text{Reg}(\vec{x})\Big],\quad\text{for}\quad p\in\{1,\,2\},
```
and

* **robust L2-deconvolution** problems, i.e.
```math
\vec{x}^*:=\text{argmin}_{\vec{x}} \Big[\sum_{i=1}^N \varrho\big( (A\vec{x} - \vec{b})_i^2 )  + \alpha\,\text{Reg}(\vec{x})\Big],
```

in 1D, 2D or 3D for a variety of different regularizers $`\text{Reg}`$ and data loss functions $`\varrho`$. 


---

The **available regularizers**, depending on the minimization problem, include
* Zeroth-order Tikhonov (TK0): $`\text{Reg}(\vec{x}) = \frac{1}{2}\Vert \vec{x} \Vert_{\ell^2}^2`$
* First-order Tikhonov (TK1): $`\text{Reg}(\vec{x}) = \frac{1}{2}\Vert \nabla \vec{x} \Vert_{\ell^2}^2`$
* Isotropic Total Variation (TV): $`\text{Reg}(\vec{x}) = \text{TV}_\text{iso}(\vec{x}) = \big\Vert |\nabla \vec{x}| \big\Vert_{\ell^1}`$
* Huber Function: $`\text{Reg}(\vec{x}) = \frac{1}{2\gamma} \big| |\nabla \vec{x}| \big|_{\gamma}`$

---

**Data loss functions** $`\varrho`$ are motivated by [SciPy](https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.least_squares.html) and allow for robust outlier rejection. Implemented data loss functions are:
* `linear`: $`\varrho(e) = e `$ 
* `soft_l1`: $`\varrho(e) = 2 (\sqrt{1+e} - 1)`$ 
* `huber`: $`\varrho(e) = |e|_\gamma = \begin{cases} e, & e < \gamma^2 \\ 2\gamma\sqrt{e} - \gamma^2, & e\ge \gamma^2\end{cases}`$
* `arctan`: $`\varrho(e) = \arctan(e)`$
* `cauchy`: $`\varrho(e) = \ln(1 + e)`$

---

Additionally, the choice of finding optimal reconstruction parameters is facilitated by providing several evaluation methods including
* **L-curve studies**, and 
* the **evaluation of similarity measures** (in case a reference image is available) 

in the course of **parameter studies**. Implemented similarity measures are

* Sum of Squared Differences (SSD)
* Mean Square Error (MSE)
* Root Mean Square Error (RMSE)
* Peak-Signal-to-Noise-Ratio (PSNR)
* Mutual Information (MI)
* Normalized Mutual Information (NMI)
* Structural Similarity (SSIM)
* Normalized Cross Correlation (NCC)

## Installation

This toolkit is currently supported for **Python 2 only** and was tested on

* Mac OS X 10.10 and 10.12
* Ubuntu 14.04 and 16.04

In case NSoL is used in conjuction with any of the toolkits of [NiftyMIC][niftymic], [Volumetric Reconstruction From Printed Films][volumetricreconstructionfromprintedfilms] or [SimpleReg][simplereg], please 
* install [ITK_NiftyMIC][itkniftymic]

If NSoL is used standalone, please run instead
* `pip install itk`

Afterwards, clone this repository via 
* `git clone git@cmiclab.cs.ucl.ac.uk:GIFT-Surg/NSoL.git`

where all remaining dependencies can be installed using `pip`:
* `pip install -r requirements.txt`
* `pip install -e .`


## Usage

### Denoising

TVL1/TVL2/HuberL2/HuberL1 Denoising can be run via

* `python runDenoising.py \
--observation path-to-observation-png-nii-mat \
--result path-to-denoised-result-png-nii-mat \
--reconstruction-type TVL1 \
--alpha 0.05 \
--iterations 50
`
* `python runDenoising.py \
--observation path-to-observation-png-nii-mat \
--reference path-to-reference-png-nii-mat \
--result path-to-denoised-result-png-nii-mat \
--reconstruction-type TVL1 \
--alpha 0.05 \
--iterations 50
`

### Deconvolution
Examples for TK0L2/TK1L2/TVL2/HuberL2 deconvolution calls are

* `python runDeconvolution.py \
--observation path-to-observation-png-nii-mat \
--result path-to-denoised-result-png-nii-mat \
--reconstruction-type HuberL2 \
--blur 1.2 \
--alpha 0.05 \
--iterations 50
`
* `python runDeconvolution.py \
--observation path-to-observation-png-nii-mat \
--reference path-to-reference-png-nii-mat \
--result path-to-denoised-result-png-nii-mat \
--reconstruction-type HuberL2 \
--alpha 0.05 \
--blur 1.2 \
--iterations 50 \
--data-loss soft_l1 \
--minimizer L-BFGS-B \
`

### Parameter Studies
Parameter studies for the denoising problem (and, similarly, for deconvolution problem) can be performed by, e.g.,
* `python runDenoisingStudy.py \
--observation path-to-observation-png-nii-mat \
--dir-output path-to-parameter-study \
--reference path-to-reference-png-nii-mat \
--reconstruction-type TVL2 \
--study-name TVL2-Denoising
`

The results can be visualized by
* `python showParameterStudy.py \
--dir-input path-to-parameter-study \
--study-name TVL2-Denoising
`

## Licensing and Copyright
Copyright (c) 2017, [University College London][ucl].
This framework is made available as free open-source software under the [BSD-3-Clause License][bsd]. Other licenses may apply for dependencies.


[mebner]: http://cmictig.cs.ucl.ac.uk/people/phd-students/michael-ebner
[tig]: http://cmictig.cs.ucl.ac.uk
[bsd]: https://opensource.org/licenses/BSD-3-Clause
[giftsurg]: http://www.gift-surg.ac.uk
[cmic]: http://cmic.cs.ucl.ac.uk
[guarantors]: https://guarantorsofbrain.org/
[ucl]: http://www.ucl.ac.uk
[uclh]: http://www.uclh.nhs.uk
[epsrc]: http://www.epsrc.ac.uk
[wellcometrust]: http://www.wellcome.ac.uk
[mssociety]: https://www.mssociety.org.uk/
[nihr]: http://www.nihr.ac.uk/research
[itkniftymic]: https://cmiclab.cs.ucl.ac.uk/GIFT-Surg/ITK_NiftyMIC/wikis/home
[niftymic]: https://cmiclab.cs.ucl.ac.uk/GIFT-Surg/NiftyMIC
[nsol]: https://cmiclab.cs.ucl.ac.uk/mebner/NSoL
[simplereg]: https://cmiclab.cs.ucl.ac.uk/mebner/SimpleReg
[simplereg-dependencies]: https://cmiclab.cs.ucl.ac.uk/GIFT-Surg/SimpleReg/wikis/simplereg-dependencies
[pysitk]: https://cmiclab.cs.ucl.ac.uk/mebner/PySiTK
[volumetricreconstructionfromprintedfilms]: https://cmiclab.cs.ucl.ac.uk/GIFT-Surg/VolumetricReconstructionFromPrintedFilms
