Summary:	A dockapp-style system load monitor
Summary(pl):	Dokowalny monitor obci±¿enia systemu
Name:		bubblefishymon
Version:	0.6.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.jnrowe.ukfsn.org/files/bfm-%{version}.tar.bz2
# Source0-md5:	91055537af29830a4852d400a43a0c45
URL:		http://www.jnrowe.ukfsn.org/projects/bfm.html
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is a dockapp-style CPU, memory, swap and load average
monitor. Based on the GNOME BubbleMon applet, this program has been
considerably improved. Many new features have been added.

%description -l pl
Ten program jest dokowalnym monitorem obci±¿enia procesora, pamiêci,
partycji wymiany oraz load average. Jest on oparty na aplecie GNOME
BubbleMon, ale od tego czasu wprowadzono wiele poprawek oraz dodano
now± funkcjonalno¶æ.

%package -n gkrellm-bubblefishymon
Summary:	Gkrellm bubblefishymon module
Summary(pl):	Modu³ bubblefishymon dla gkrellm
Group:		X11/Applications
Requires:	gkrellm

%description -n gkrellm-bubblefishymon
This program is a dockapp-style CPU, memory, swap and load average
monitor. Based on the GNOME BubbleMon applet, this program has been
considerably improved. Many new features have been added. This is
gkrellm version of bubblefishymon.

%description -n gkrellm-bubblefishymon -l pl
Ten program jest dokowalnym monitorem obci±¿enia procesora, pamiêci,
partycji wymiany oraz load average. Jest on oparty na aplecie GNOME
BubbleMon, ale od tego czasu wprowadzono wiele poprawek oraz dodano
now± funkcjonalno¶æ. Ten pakiet zawiera wersjê programu dla gkrellm.

%prep
%setup -q -n bfm-%{version}

%build
%{__make} PREFIX=%{_prefix}
%{__make} gkrellm

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} -D gkrellm-bfm.so \
	$RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/bubblefishymon.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* README* SUPPORTED_SYSTEMS TODO doc/Xdefaults.sample
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*

%files -n gkrellm-bubblefishymon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/*.so
