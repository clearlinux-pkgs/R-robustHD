#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-robustHD
Version  : 0.7.3
Release  : 13
URL      : https://cran.r-project.org/src/contrib/robustHD_0.7.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/robustHD_0.7.3.tar.gz
Summary  : Robust Methods for High-Dimensional Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-robustHD-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-ggplot2
Requires: R-perry
Requires: R-robustbase
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-ggplot2
BuildRequires : R-lars
BuildRequires : R-perry
BuildRequires : R-robustbase
BuildRequires : buildreq-R

%description
model selection techniques based on least angle regression and sparse
    regression.

%package lib
Summary: lib components for the R-robustHD package.
Group: Libraries

%description lib
lib components for the R-robustHD package.


%prep
%setup -q -n robustHD
cd %{_builddir}/robustHD

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660318491

%install
export SOURCE_DATE_EPOCH=1660318491
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/robustHD/CITATION
/usr/lib64/R/library/robustHD/DESCRIPTION
/usr/lib64/R/library/robustHD/INDEX
/usr/lib64/R/library/robustHD/Meta/Rd.rds
/usr/lib64/R/library/robustHD/Meta/data.rds
/usr/lib64/R/library/robustHD/Meta/features.rds
/usr/lib64/R/library/robustHD/Meta/hsearch.rds
/usr/lib64/R/library/robustHD/Meta/links.rds
/usr/lib64/R/library/robustHD/Meta/nsInfo.rds
/usr/lib64/R/library/robustHD/Meta/package.rds
/usr/lib64/R/library/robustHD/NAMESPACE
/usr/lib64/R/library/robustHD/NEWS
/usr/lib64/R/library/robustHD/R/robustHD
/usr/lib64/R/library/robustHD/R/robustHD.rdb
/usr/lib64/R/library/robustHD/R/robustHD.rdx
/usr/lib64/R/library/robustHD/data/TopGear.RData
/usr/lib64/R/library/robustHD/data/datalist
/usr/lib64/R/library/robustHD/data/nci60.RData
/usr/lib64/R/library/robustHD/doc/examples/example-AIC.R
/usr/lib64/R/library/robustHD/doc/examples/example-coef.R
/usr/lib64/R/library/robustHD/doc/examples/example-coefPlot.R
/usr/lib64/R/library/robustHD/doc/examples/example-critPlot.R
/usr/lib64/R/library/robustHD/doc/examples/example-diagnosticPlot.R
/usr/lib64/R/library/robustHD/doc/examples/example-fitted.R
/usr/lib64/R/library/robustHD/doc/examples/example-fortify.R
/usr/lib64/R/library/robustHD/doc/examples/example-lambda0.R
/usr/lib64/R/library/robustHD/doc/examples/example-perry.R
/usr/lib64/R/library/robustHD/doc/examples/example-plot.R
/usr/lib64/R/library/robustHD/doc/examples/example-predict.R
/usr/lib64/R/library/robustHD/doc/examples/example-residuals.R
/usr/lib64/R/library/robustHD/doc/examples/example-rgrplars.R
/usr/lib64/R/library/robustHD/doc/examples/example-rlars.R
/usr/lib64/R/library/robustHD/doc/examples/example-setupCoefPlot.R
/usr/lib64/R/library/robustHD/doc/examples/example-setupCritPlot.R
/usr/lib64/R/library/robustHD/doc/examples/example-setupDiagnosticPlot.R
/usr/lib64/R/library/robustHD/doc/examples/example-sparseLTS.R
/usr/lib64/R/library/robustHD/doc/examples/example-weights.R
/usr/lib64/R/library/robustHD/help/AnIndex
/usr/lib64/R/library/robustHD/help/aliases.rds
/usr/lib64/R/library/robustHD/help/paths.rds
/usr/lib64/R/library/robustHD/help/robustHD.rdb
/usr/lib64/R/library/robustHD/help/robustHD.rdx
/usr/lib64/R/library/robustHD/html/00Index.html
/usr/lib64/R/library/robustHD/html/R.css
/usr/lib64/R/library/robustHD/tests/testthat.R
/usr/lib64/R/library/robustHD/tests/testthat/test-fastLasso-highdim.R
/usr/lib64/R/library/robustHD/tests/testthat/test-fastLasso-multiple.R
/usr/lib64/R/library/robustHD/tests/testthat/test-fastLasso-simple.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/robustHD/libs/robustHD.so
/usr/lib64/R/library/robustHD/libs/robustHD.so.avx2
/usr/lib64/R/library/robustHD/libs/robustHD.so.avx512
