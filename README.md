# Replication: Michael P. Keane & Kenneth I. Wopin
This notebook replicates results from:

Keane, M. P. & Wopin, W. I. (1997). [The career Decisions of Young Men.](https://www.jstor.org/stable/10.1086/262080), 
*Journal of Political Economy, 105(3): 473-552.*105(3): 473-552.

For this purpose l rely on the  *respy* and *estimagic* open-source python packages. [*Respy*](https://github.com/OpenSourceEconomics/respy) is for the simulation and estimation of a prototypical finite-horizon discrete choice dynamic programming model and [*Estimagic*](https://github.com/OpenSourceEconomics/estimagic) helps to build high-quality and user friendly implementations of (structural) econometric models.

## Motivation for replicating KW1997

Often times, the research outcomes that emerge from data in the developed world's context do not easily replicate in a developing country setting. However, many lessons could be drawn from them to learn something about human capital formation for low income countries (LICs). I chose to replicate this paper to learn more about structural econometric methods in a human capital formation setting. I hope to apply my knowledge to address questions, in the future, such as how to increase the level of skill acquired in the higher education system such that the up and coming generation of the African workforce is well equiped for competent roles in the labour market. Ultimately, this could inform policy to help achieve the African Union's 2063 vision - to build an intergrated, prosperous and peaceful Africa, driven by its own citizens.

## Project structure

In **section I**, l give an introduction to the project, my motivation for replicating KW1997 as well what motivates the paper. I replicate the descriptive statistics of the data and illustrate them graphically in **section II**. It should be kept in mind whilst interpreting the graphs, that as the number of periods increase, sample attrition plays a role. In **section III**, l discuss the theoretical framework of the paper, which ties back to the descriptive statistics in section 2, as well as develop a causal graphical framework for the model. I then reproduce the main results in **section IV** using the *respy* and *estimagic* packages and calculate standard errors for the estimated parameters. In **section V**, l do a simulation study that extends the number of periods from 11 to 40. This enables me to compare the basic and extended model predictions with respect to choice and age. In **section VI**, l discuss the results of the paper and a short assessment of the extended model which in turn concludes my contribution to the replication of KW1997.

## Authors

* **Linda Maokomatanda** 

## Acknowledgments

* Respy contributors
* Estimagic contributors
* Microeconometrics professor (Philipp Eisenhauer) & team

## References

- Keane, M. P. & Wopin, W. I. (1997). [The career Decisions of Young Men.](https://www.jstor.org/stable/10.1086/262080)
 *Journal of Political Economy, 105(3): 473-552.*
 
- Keane, M. P. & Wopin, W. I., & Vytlacil, E. J. (1994). 
[The Solution and Estimation of Discrete Choice Dynamic Programming Models by Simulation and Interpolation: Monte Carlo Evidence.](https://www.jstor.org/stable/2109768)  *The Review of Economics and Statistics, 76(4): 648-672.*

- Marno Verbeek. A Guide to Modern Econometrics, *Fifth Edition*.

- [Statmodels implementation of the HJJH covariance matrix](https://tinyurl.com/yym5d4cw).



[![Build Status](https://travis-ci.org/HumanCapitalAnalysis/student-project-lindamaok899.svg?branch=lindamaok899)](https://travis-ci.org/HumanCapitalAnalysis/student-project-lindamaok899) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](HumanCapitalAnalysis/student-project-template/blob/master/LICENSE)
