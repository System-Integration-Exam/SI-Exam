#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Reservation.csproj", "."]
RUN dotnet restore "Reservation.csproj"
COPY . .
RUN dotnet build "Reservation.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Reservation.csproj" -c Release -o /app/publish

FROM base AS final

LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam
ENV ASPNETCORE_URLS=http://+:5000
EXPOSE 5000
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Reservation.dll"]