package com.javainuse.model;


import java.util.Objects;

public class ICE {

    private double vehiclePrice;
    private double maintenanceCost;
    private double lifelongMiles;
    private double milesPerGallon;
    private double dollarsPerGallon;
    private double milesPerDay;
    private double daysPerYear;
    public ICE(){

    }

    public double getVehiclePrice() {
        return vehiclePrice;
    }

    public void setVehiclePrice(double vehiclePrice) {
        this.vehiclePrice = vehiclePrice;
    }

    public double getMaintenanceCost() {
        return maintenanceCost;
    }

    public void setMaintenanceCost(double maintenanceCost) {
        this.maintenanceCost = maintenanceCost;
    }

    public double getLifelongMiles() {
        return lifelongMiles;
    }

    public void setLifelongMiles(double lifelongMiles) {
        this.lifelongMiles = lifelongMiles;
    }

    public double getMilesPerGallon() {
        return milesPerGallon;
    }

    public void setMilesPerGallon(double milesPerGallon) {
        this.milesPerGallon = milesPerGallon;
    }

    public double getDollarsPerGallon() {
        return dollarsPerGallon;
    }

    public void setDollarsPerGallon(double dollarsPerGallon) {
        this.dollarsPerGallon = dollarsPerGallon;
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

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof ICE)) return false;
        ICE ice = (ICE) o;
        return Double.compare(ice.getVehiclePrice(), getVehiclePrice()) == 0 &&
                Double.compare(ice.getMaintenanceCost(), getMaintenanceCost()) == 0 &&
                Double.compare(ice.getLifelongMiles(), getLifelongMiles()) == 0 &&
                Double.compare(ice.getMilesPerGallon(), getMilesPerGallon()) == 0 &&
                Double.compare(ice.getDollarsPerGallon(), getDollarsPerGallon()) == 0 &&
                Double.compare(ice.getMilesPerDay(), getMilesPerDay()) == 0 &&
                Double.compare(ice.getDaysPerYear(), getDaysPerYear()) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(getVehiclePrice(), getMaintenanceCost(), getLifelongMiles(), getMilesPerGallon(), getDollarsPerGallon(),
                getMilesPerDay(), getDaysPerYear());
    }

    @Override
    public String toString() {
        return "ICE{" +
                "vehiclePrice=" + vehiclePrice +
                ", maintenanceCost=" + maintenanceCost +
                ", lifelongMiles=" + lifelongMiles +
                ", milesPerGallon=" + milesPerGallon +
                ", dollarsPerGallon=" + dollarsPerGallon +
                ", milesPerDay=" + milesPerDay +
                ", daysPerYear=" + daysPerYear +
                '}';
    }
}
