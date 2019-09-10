package com.javainuse.model;

import java.util.Objects;

public class EV {

    private double vehiclePrice;
    private double evMaintenanceSaving;
    private double infrastructureUpgrade; 
    private double lifelongMiles;
    private double milesPerKWH;
    private double dollarsPerKWH;
    private double batteryLeasingCost;
    private double batteryReplacementCost;
    private double milesPerDay;
    private double daysPerYear;
    private double iceMaintenanceCost;

    public EV(){

    }

    public double getVehiclePrice() {
        return vehiclePrice;
    }

    public void setVehiclePrice(double vehiclePrice) {
        this.vehiclePrice = vehiclePrice;
    }

    public double getEvMaintenanceSaving() {
        return evMaintenanceSaving;
    }

    public void setEvMaintenanceSaving(double evMaintenanceSaving) {
        this.evMaintenanceSaving = evMaintenanceSaving;
    }

    public double getInfrastructureUpgrade() {
        return infrastructureUpgrade;
    }

    public void setInfrastructureUpgrade(double infrastructureUpgrade) {
        this.infrastructureUpgrade = infrastructureUpgrade;
    }

    public double getLifelongMiles() {
        return lifelongMiles;
    }

    public void setLifelongMiles(double lifelongMiles) {
        this.lifelongMiles = lifelongMiles;
    }

    public double getMilesPerKWH() {
        return milesPerKWH;
    }

    public void setMilesPerKWH(double milesPerKWH) {
        this.milesPerKWH = milesPerKWH;
    }

    public double getDollarsPerKWH() {
        return dollarsPerKWH;
    }

    public void setDollarsPerKWH(double dollarsPerKWH) {
        this.dollarsPerKWH = dollarsPerKWH;
    }

    public double getBatteryLeasingCost() {
        return batteryLeasingCost;
    }

    public void setBatteryLeasingCost(double batteryLeasingCost) {
        this.batteryLeasingCost = batteryLeasingCost;
    }

    public double getBatteryReplacementCost() {
        return batteryReplacementCost;
    }

    public void setBatteryReplacementCost(double batteryReplacementCost) {
        this.batteryReplacementCost = batteryReplacementCost;
    }

    public double getMilesPerDay() {
        return milesPerDay;
    }

    public void setMilesPerDay(double milesPerDay) {
        this.milesPerDay = milesPerDay;
    }

    public double getDaysPerYear() {
        return daysPerYear;
    }

    public void setDaysPerYear(double daysPerYear) {
        this.daysPerYear = daysPerYear;
    }

    public double getIceMaintenanceCost() {
        return iceMaintenanceCost;
    }

    public void setIceMaintenanceCost(double iceMaintenanceCost) {
        this.iceMaintenanceCost = iceMaintenanceCost;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof EV)) return false;
        EV ev = (EV) o;
        return Double.compare(ev.getVehiclePrice(), getVehiclePrice()) == 0 &&
                Double.compare(ev.getEvMaintenanceSaving(), getEvMaintenanceSaving()) == 0 &&
                Double.compare(ev.getInfrastructureUpgrade(), getInfrastructureUpgrade()) == 0 &&
                Double.compare(ev.getLifelongMiles(), getLifelongMiles()) == 0 &&
                Double.compare(ev.getMilesPerKWH(), getMilesPerKWH()) == 0 &&
                Double.compare(ev.getDollarsPerKWH(), getDollarsPerKWH()) == 0 &&
                Double.compare(ev.getBatteryLeasingCost(), getBatteryLeasingCost()) == 0 &&
                Double.compare(ev.getBatteryReplacementCost(), getBatteryReplacementCost()) == 0 &&
                Double.compare(ev.getMilesPerDay(), getMilesPerDay()) == 0 &&
                Double.compare(ev.getDaysPerYear(), getDaysPerYear()) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(getVehiclePrice(), getEvMaintenanceSaving(), getInfrastructureUpgrade(), getLifelongMiles(),
                getMilesPerKWH(), getDollarsPerKWH(), getBatteryLeasingCost(), getBatteryReplacementCost(),
                getMilesPerDay(), getDaysPerYear());
    }

    @Override
    public String toString() {
        return "EV{" +
                "vehiclePrice=" + vehiclePrice +
                ", evMaintenanceSaving=" + evMaintenanceSaving +
                ", infrastructureUpgrade=" + infrastructureUpgrade +
                ", lifelongMiles=" + lifelongMiles +
                ", milesPerKWH=" + milesPerKWH +
                ", dollarsPerKWH=" + dollarsPerKWH +
                ", batteryLeasingCost=" + batteryLeasingCost +
                ", batteryReplacementCost=" + batteryReplacementCost +
                ", milesPerDay=" + milesPerDay +
                ", daysPerYear=" + daysPerYear +
                ", iceMaintenanceCost=" + iceMaintenanceCost +
                '}';
    }
}
