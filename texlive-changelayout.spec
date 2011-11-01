Name:		texlive-changelayout
Version:	1.0
Release:	1
Summary:	Change the layout of individual pages and their text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changelayout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelayout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelayout.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is an extension of the changepage package to permit
the user to change the layout of individual pages and their
texts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
