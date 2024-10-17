Name:		texlive-lexref
Version:	36026
Release:	2
Summary:	Convenient and uniform references to legal provisions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lexref
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexref.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
