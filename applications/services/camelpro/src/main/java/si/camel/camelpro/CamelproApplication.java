package si.camel.camelpro;

import org.apache.camel.CamelContext;
import org.apache.camel.impl.DefaultCamelContext;


public class CamelproApplication {


    public static void main(String[] args) {

            try {
                CamelContext context = new DefaultCamelContext();
                ConverterRoute route = new ConverterRoute();
                route.addRoutesToCamelContext(context);
                context.start();

                Thread.sleep(10000);
                context.stop();
            } catch (Exception exe) {

                exe.printStackTrace();
            }


    }

}
