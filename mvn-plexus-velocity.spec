#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-velocity
Version  : 1.1.7
Release  : 2
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.pom
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.8/plexus-velocity-1.1.8.jar
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-velocity/1.1.8/plexus-velocity-1.1.8.pom
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.jar
Source5  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plexus-velocity-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-velocity package.
Group: Data

%description data
data components for the mvn-plexus-velocity package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.7
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.8
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.8

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.8
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.8

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.2


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.7/plexus-velocity-1.1.7.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.8/plexus-velocity-1.1.8.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.1.8/plexus-velocity-1.1.8.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.pom
