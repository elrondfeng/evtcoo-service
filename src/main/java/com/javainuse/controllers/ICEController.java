package com.javainuse.controllers;

import com.javainuse.model.ICE;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;

@CrossOrigin(origins = "http://localhost:4200")
@RestController
@RequestMapping({ "/ice" })
public class ICEController {

    private static final Logger logger = LoggerFactory.getLogger(EVController.class);

    @PostMapping(produces = "application/json")
    public double calculateICEDollarPerMile(@RequestBody ICE ice) {
        logger.debug("this is the parameter of ICE " + ice.toString());
        return calculate(ice);
    }

    private double calculate(ICE ice){

        double C15 = ice.getVehiclePrice(); logger.debug("c15 " + C15);
        double C17 = ice.getLifelongMiles(); logger.debug("c17 " + C17);
        double C23 = ice.getMilesPerDay(); logger.debug("c23 " + C23);
        double C24 = ice.getDaysPerYear(); logger.debug("c24 " + C24);
        double C18 = ice.getMilesPerGallon(); logger.debug("c18 " + C18);
        double C19 = ice.getDollarsPerGallon(); logger.debug("c19 " + C19);
        double C16 = ice.getMaintenanceCost(); logger.debug("c16 " + C16);

        double result = (C15/(C17/(C23*C24))+(C23*C24)/C18*C19+C16*C23*C24)/(C23*C24);

        logger.debug("the result is " + result);

        return result;
    }

    // ICE{vehiclePrice=60000.0, maintenanceCost=0.302, lifelongMiles=200000.0, MPG=0.0, dollarsPerGallon=2.73, milesPerDay=70.0, daysPerYear=240.0}


}
