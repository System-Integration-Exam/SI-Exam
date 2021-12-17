package si.camel.camelpro;


import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.CamelContext;
import org.apache.camel.dataformat.csv.CsvDataFormat;
import org.apache.camel.impl.DefaultCamelContext;
import org.apache.camel.model.dataformat.JsonLibrary;


public class CamelproApplication {

    public static void main(String[] args) {
        try {
            CamelContext context = SetupCamelContext();
            context.start();
            Thread.sleep(10000);
            context.stop();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    static CamelContext SetupCamelContext() throws Exception {
        CamelContext context = new DefaultCamelContext();

        context.addRoutes(new RouteBuilder() {
            public void configure() {
                CsvDataFormat csvDataFormat = new CsvDataFormat();
                csvDataFormat.setHeaderDisabled(true);
                csvDataFormat.setDelimiter(',');
                csvDataFormat.setQuoteDisabled(true);

                from("file:src/main/resources/csvdata/?noop=true")
                    .unmarshal()
                    .csv()
                    .marshal()
                    .json(JsonLibrary.Jackson)
                    .log("${body}")
                    .to("kafka:subscriptionserviceuserlistupdate-topic?brokers=kafka-service:9092")
                    .end();
            }
        });

        return context;
    }
}
