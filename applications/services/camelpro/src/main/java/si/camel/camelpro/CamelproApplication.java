package si.camel.camelpro;

import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.CamelContext;
import org.apache.camel.dataformat.csv.CsvDataFormat;
import org.apache.camel.impl.DefaultCamelContext;
import org.apache.camel.model.dataformat.JsonLibrary;

import java.io.InputStream;
import java.util.Properties;

public class CamelproApplication {

    static String _csvPath;
    static String _kafkaBroker;

    public static void main(String[] args) {
        try {
            loadProperties();

            CamelContext context = setupCamelContext();

            context.start();
            Thread.sleep(10000);
            context.stop();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    static void loadProperties() throws Exception{
        Properties props = new Properties();
        InputStream input = CamelproApplication.class.getClassLoader().getResourceAsStream("application.properties");
        props.load(input);

        _csvPath = props.getProperty("csv_path");
        _kafkaBroker = props.getProperty("kafka_broker");
    }

    static CamelContext setupCamelContext() throws Exception {
        CamelContext context = new DefaultCamelContext();

        context.addRoutes(new RouteBuilder() {
            public void configure() {
                CsvDataFormat csvDataFormat = new CsvDataFormat();
                csvDataFormat.setHeaderDisabled(true);
                csvDataFormat.setDelimiter(',');
                csvDataFormat.setQuoteDisabled(true);

                from("file:" + _csvPath + "?noop=true")
                    .unmarshal()
                    .csv()
                    .marshal()
                    .json(JsonLibrary.Jackson)
                    .log("${body}")
                    .to("kafka:subscriptionserviceuserlistupdate-topic?brokers=" + _kafkaBroker)
                    .end();
            }
        });

        return context;
    }
}
