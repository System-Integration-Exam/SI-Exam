package si.camel.camelpro;

import org.apache.camel.CamelContext;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.dataformat.csv.CsvDataFormat;

import org.apache.camel.model.dataformat.JsonLibrary;

public class ConverterRoute {

    public void addRoutesToCamelContext(CamelContext context) throws Exception {
        context.addRoutes(new RouteBuilder() {
            public void configure() {
                try {
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
                } catch (Exception e) {
                    e.printStackTrace();
                    throw e;
                }
            }
        });
    }
}
