import React, { Component } from "react";
import union from "folktale/adt/union/union";

const FetchState = union("FetchState", {
    PreFetch: () => ({}),
    Fetched: value => ({ value }),
    Fail: error => ({ error })
});

const { PreFetch, Fetched, Fail } = FetchState;

export class Kmom01 extends Component {
    constructor() {
        super();
        this.state = {
            malmoGenerate: PreFetch(),
            malmoTable: PreFetch(),
            malmoImage: PreFetch()
        };
    }

    componentDidMount() {
        fetch("/api/assignment/1/malmonow-generate")
            .then(res => res.json())
            .then(({ time }) => this.setState(() => ({ malmoGenerate: Fetched(time) })))
            .then(() => fetch("/api/assignment/1/malmonow-image"))
            .then(res => res.blob())
            .then(blob => this.setState(() => ({ malmoImage: Fetched(URL.createObjectURL(blob)) })))
            .then(() => fetch("/api/assignment/1/malmonow-text"))
            .then(res => res.text())
            .then(text => this.setState(() => ({ malmoTable: Fetched(text) })))
            .catch(e => this.setState(() => ({ malmoTable: Fail(e) })));
    }

    render() {
        const updated = this.state.malmoGenerate.matchWith({
            PreFetch: () => "uppdaterar...",
            Fail: ({ e }) => `Något gick galet:\n${e}`,
            Fetched: ({ value }) => new Date(value).toLocaleString("sv")
        });
        const image = this.state.malmoImage.matchWith({
            PreFetch: () => <span>"Hämtar diagram..."</span>,
            Fail: ({ e }) => <span>`Något gick galet:\n${e}`</span>,
            Fetched: ({ value }) => (
                <img className="img-100" src={value} alt="Temperatur Malmö senaste timmen" />
            )
        });
        const textTable = this.state.malmoTable.matchWith({
            PreFetch: () => "Hämtar tabell...",
            Fail: ({ e }) => `Något gick galet:\n${e}`,
            Fetched: ({ value }) => value
        });

        return (
            <div>
                <h1>Uppgift1</h1>
                <p className="text-small text-italic">Tidsserie uppdaterad: {updated}</p>

                <p>
                    Som tidsserie har jag valt det senaste dygnets temperaturer i Malmö hämtade från
                    SMHI:s api.
                </p>
                <p>
                    Diagrammets rubrik visar mätstationens namn och vilket tidsintervall som
                    hämtats.
                </p>
                <p className="center">{image}</p>

                <p>{this.state.malmoImg}</p>

                <h2>Tabell genererad från python-skript</h2>
                <pre className="text-small center">{textTable}</pre>

                <br />
                <h2>Kort reflektion</h2>
                <h3>Derivatan</h3>
                <p>
                    I denna tidserie beskriver derivatan temparaturförändringen vid en given timme.
                </p>
                <p>
                    Den centrala derivatan ger den bästa approximationen. I just detta fallet kan
                    det vara intressant att notera att derivatan framåt ger en historisk
                    temperaturprognos med 100% träffsäkerhet.
                </p>
                <h3>Glidande medelvärde</h3>
                <p>
                    Ett glidande medelvärde kan hjälpa till att jämna ut en kurva så det tex kan
                    vara enklare att se trender. För en tidserie som representerar temperaturer över
                    ett dygn har jag svårt att se att ett glidande medelvärde tillför något.
                    Förmodligen är det annorlunda med längre tidsserier, tex årstemperaturer sedan
                    150 år tillbaka. Där kan ett glidande medelvärde göra att graferna blir lättare
                    att tolka då kurvan jämnar ut stora avvikelser.
                </p>
            </div>
        );
    }
}
