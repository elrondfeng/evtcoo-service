package com.javainuse.controllers;

import com.javainuse.model.EV;
import org.springframework.web.bind.annotation.*;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@CrossOrigin(origins = "http://localhost:4200")
@RestController
@RequestMapping({"/ev"})

public class EVController {

    private static final Logger logger = LoggerFactory.getLogger(EVController.class);

    @PostMapping(produces = "application/json")
    public double calculateEVDollarPerMile(@RequestBody EV ev) {
        logger.debug("got called ********  "+ ev.toString());
        return calculate(ev);
    }

    private double calculate(EV ev) {
        double C3 = ev.getVehiclePrice();
        double C10 = ev.getBatteryReplacementCost();
        double C6 = ev.getLifelongMiles();
        double C23 = ev.getMilesPerDay();
        double C24 = ev.getDaysPerYear();
        double C7 = ev.getMilesPerKWH();
        double C8 = ev.getDollarsPerKWH();
        double C5 = ev.getInfrastructureUpgrade();
        double C4 = ev.getEvMaintenanceSaving();
        double C16 = ev.getIceMaintenanceCost();
        double C9 = ev.getBatteryLeasingCost();

        return ((C3 + C10) / (C6 / (C23 * C24)) + (C23 * C24) / C7 * C8 + C5 + (1 - C4) * C16 * C23 * C24) / (C23 * C24) + C9;
    }

}
