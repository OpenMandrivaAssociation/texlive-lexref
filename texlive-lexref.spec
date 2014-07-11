# revision 32751
# category Package
# catalog-ctan /macros/latex/contrib/lexref
# catalog-date 2014-01-21 18:42:00 +0100
# catalog-license lppl1.3
# catalog-version 1.0.1 alpha
Name:		texlive-lexref
Version:	1.0.1alpha
Release:	3
Summary:	Convenient and uniform references to legal provisions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lexref
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexref.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is aimed at continental lawyers (especially those
in Switzerland and Germany), allowing the user to make
references to legal provisions conveniently and uniformly. The
package also allows the user to add cited Acts to a
nomenclature list (automatically), and to build specific
indexes for each cited Act. The package is still under
development, and should be treated as an 'alpha'-release.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lexref/lexref.sty
%doc %{_texmfdistdir}/doc/latex/lexref/README
%doc %{_texmfdistdir}/doc/latex/lexref/lexref.pdf
%doc %{_texmfdistdir}/doc/latex/lexref/lexref.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
