%global packname  TeachingDemos
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.9
Release:          1
Summary:          Demonstrations for teaching and learning
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/TeachingDemos_2.9.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-tkrplot R-lattice R-MASS R-rgl R-sgeostat R-mapproj R-tcltk R-tcltk2 R-EBImage R-png 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-tkrplot R-lattice R-MASS R-rgl R-sgeostat R-mapproj R-tcltk R-tcltk2 R-EBImage R-png 

%description
This package is a set of demonstration functions that can be used in a
classroom to demonstrate statistical concepts, or on your own to better
understand the concepts or the programming.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
