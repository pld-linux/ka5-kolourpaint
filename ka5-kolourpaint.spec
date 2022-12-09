#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kolourpaint
Summary:	kolourpaint
Name:		ka5-%{kaname}
Version:	22.12.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a966b58e2bc9e3d1b22741937aef949e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libksane-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KolourPaint is a simple painting program to quickly create raster
images. It is useful as a touch-up tool and simple image editing
tasks.

Features: Support for drawing various shapes - lines, rectangles,
rounded rectangles, ovals and polygons.

%description -l pl.UTF-8
KolourPaint jest prostym programem do szybkiego tworzenia
rastrowych obrazków. Jest przydatny do retuszowania i prostych
zadań edycji obrazków.

Właściwości: Wsparcie dla rysowania różnych kształtów - linii,
prostokątów, zaokrąglonych prostokątów, owali i wieloboków.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/tok

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolourpaint
%{_libdir}/libkolourpaint_lgpl.so
%attr(755,root,root) %{_libdir}/libkolourpaint_lgpl.so.5
%{_desktopdir}/org.kde.kolourpaint.desktop
%{_iconsdir}/hicolor/16x16/apps/kolourpaint.png
%{_iconsdir}/hicolor/22x22/apps/kolourpaint.png
%{_iconsdir}/hicolor/32x32/apps/kolourpaint.png
%{_iconsdir}/hicolor/48x48/apps/kolourpaint.png
%{_iconsdir}/hicolor/scalable/apps/kolourpaint.svgz
%{_datadir}/kolourpaint
%{_datadir}/kxmlgui5/kolourpaint
%{_datadir}/metainfo/org.kde.kolourpaint.appdata.xml
%{_iconsdir}/hicolor/128x128/apps/kolourpaint.png
