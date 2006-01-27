Summary:	Initconf - Gnome GUI for initng
Summary(pl):	Initconf - graficzny interfejs u¿ytkownika GNOME dla initng
Name:		initng-initconf
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	http://www.folkbildning.net/~daniel.malmgren/initconf-%{version}.tar.gz
# Source0-md5:	6975fea7d1344085e703829be7d1a5a5
BuildRequires:	libgnomeui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome GUI for configuring initng. It's in a _very_ early development
stage at the time of writing. Please feel free to contribute ;-)

%description -l pl
Graficzny interfejs u¿ytkownika GNOME do konfiguracji initng. Jest
jeszcze w _bardzo_ wczesnym stadium rozwoju, pomoc mile widziana.

%prep
%setup -q -n initconf-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/initconf
