# revision 16094
# category Package
# catalog-ctan /macros/latex/contrib/changelayout
# catalog-date 2009-11-09 14:16:05 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-changelayout
Version:	1.0
Release:	4
Summary:	Change the layout of individual pages and their text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changelayout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelayout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelayout.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750096
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718030
- texlive-changelayout
- texlive-changelayout
- texlive-changelayout
- texlive-changelayout
- texlive-changelayout

