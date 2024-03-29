Summary:	Make replacement from Plan 9
Summary(pl.UTF-8):	Zamiennik make z Plan 9
Name:		mk
Version:	1.5
Epoch:		1
Release:	1
License:	distributable
Group:		Development/Building
Vendor:		Norman Ramsey <nr@eecs.harvard.edu>
Source0:	http://www.cminusminus.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	713b737855f84005bfb2821aba87fcce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet another make(1) replacement. This one comes from Plan 9, and is
used to build QC--.

%description -l pl.UTF-8
Jeszcze jeden zamiennik make(1). Pochodzi z systemu Plan 9, i jest
używany do budowania QC--.

%prep
%setup -q 

%build
%{__make} \
	 CC="%{__cc} %{rpmcflags} -ansi"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

install mk.1 $RPM_BUILD_ROOT%{_mandir}/man1
install mk $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mk.pdf README LICENCE CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
