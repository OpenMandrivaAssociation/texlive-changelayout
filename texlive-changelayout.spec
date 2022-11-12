Name:		texlive-changelayout
Version:	16094
Release:	1
Summary:	Change the layout of individual pages and their text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changelayout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelayout.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelayout.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is an extension of the changepage package to permit
the user to change the layout of individual pages and their
texts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/changelayout/changelayout.sty
%doc %{_texmfdistdir}/doc/latex/changelayout/README
%doc %{_texmfdistdir}/doc/latex/changelayout/changelayout-guide.pdf
%doc %{_texmfdistdir}/doc/latex/changelayout/changelayout-guide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
