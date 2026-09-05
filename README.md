# NetAtlas Flow Analyzer: Interactive Network Topology & Traffic Visualizer GUI

![Language](https://img.shields.io/badge/Language-Python-blue.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![AI Generated](https://img.shields.io/badge/Content-AI_Generated-orange.svg?style=for-the-badge&logo=openai)

## Architecture Overview & Problem Statement

In an era of increasingly complex and dynamic network infrastructures, maintaining real-time visibility into network topology, device health, and traffic flow is paramount for operational efficiency, security, and performance optimization. Traditional network monitoring solutions often present static views or overwhelming raw data, making proactive issue identification and rapid troubleshooting a significant challenge for network administrators and engineers.

The **NetAtlas Flow Analyzer** addresses this critical need by providing an interactive, real-time desktop GUI application built on Python. It employs a multi-faceted approach to discover, map, and visualize your network. At its core, NetAtlas integrates robust network discovery mechanisms with a responsive graphical interface to translate raw network telemetry into actionable visual insights. The architecture is designed for modularity, allowing for flexible integration of various data sources (e.g., SNMP, ARP, custom agents) and rendering them within a dynamic Tkinter-based user interface. This ensures that network health, topology changes, and traffic anomalies are immediately apparent, empowering users with comprehensive situational awareness and facilitating rapid incident response.

## Features

NetAtlas Flow Analyzer delivers a powerful suite of capabilities designed for deep network insight:

*   **Real-time Topology Discovery & Dynamic Mapping**: Automatically scans and identifies network devices (routers, switches, endpoints) and their interconnections, rendering a live, interactive topological map. The map dynamically updates to reflect changes in network configuration, device status, and link state without manual intervention.
*   **Interactive Traffic Flow Visualization**: Provides granular and aggregate traffic flow monitoring directly on the network diagram. Visualize real-time bandwidth utilization, packet counts, and flow direction between any two nodes, with drill-down capabilities to inspect specific data streams and their characteristics.
*   **Comprehensive Device Health Monitoring**: Integrates robust monitoring for critical device health metrics, including CPU utilization, memory usage, interface status (up/down, errors), and uptime. Health indicators are visually integrated into the topology, offering immediate alerts and simplifying the identification of stressed or failing network components.
*   **Deep Packet Inspection & Analysis**: Facilitates the capture and detailed dissection of network packets traversing selected links or nodes. Users can inspect full packet headers, identify protocols, source/destination IPs and ports, and even preview payload data, enabling advanced troubleshooting, security forensics, and performance bottleneck analysis.
*   **Dynamic & Customizable User Interface**: Features an intuitive, interactive GUI developed with Tkinter, offering dynamic node diagrams with draggable elements, smooth pan/zoom functionalities, and live-updating charts for key network metrics. A professionally designed dark-mode theme enhances readability and reduces eye strain during extended monitoring sessions.
*   **Extensible Telemetry & Protocol Support**: Engineered with an extensible framework to support various network telemetry sources and protocols (e.g., SNMP, ARP, potentially NetFlow/IPFIX via future modules). This modular design ensures adaptability to evolving network environments and allows for future integration of custom data providers.

## Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8+**: NetAtlas is developed and tested with recent Python versions.
*   **Operating System**: Linux, macOS, or Windows.
*   **Network Permissions**: The application requires appropriate network access permissions to perform discovery (e.g., raw socket access for ARP/packet capture, SNMP access if configured).

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/netatlas-flow-analyzer.git
    cd netatlas-flow-analyzer
    ```

2.  **Install Dependencies**:
    It is highly recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    *   *Note*: The `requirements.txt` typically includes libraries like `scapy` for packet manipulation, `psutil` for system health, `pysnmp` for SNMP interactions, `matplotlib` for charting, and `Pillow` for image handling.

### Usage

1.  **Activate Virtual Environment (if not already)**:
    ```bash
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

2.  **Run the Application**:
    ```bash
    python gui_app.py
    ```
    This command will launch the interactive NetAtlas Flow Analyzer GUI window.

## Example Telemetry Output

Upon successful launch, NetAtlas will initialize its discovery engines and begin populating the visual network topology. Below is a conceptual representation of the type of real-time insights you would observe within the GUI and minimal console feedback.

```
# Console output upon launching the application:
[INFO] 2023-10-27 10:30:01 - Initializing NetAtlas Flow Analyzer GUI...
Launched visual GUI application window [Tkinter] with interactive network visualization
[INFO] 2023-10-27 10:30:03 - Starting network discovery scan...

# --- Inside the GUI Window (Visual Representation) ---

## Live Network Topology Map:
(Dynamic graphical representation of nodes and links, updating in real-time)

- **Node**: `Router-Edge` (IP: 192.168.1.1, Type: Router)
  - **Status**: ✅ Healthy
  - **CPU Load**: 12% | **Memory Util**: 25%
  - **Interfaces**: eth0 (UP, 100Mbps), eth1 (UP, 1000Mbps)
  - **Traffic**: 🌐 45 Mbps IN / 30 Mbps OUT
- **Node**: `Switch-Core` (IP: 192.168.1.2, Type: Switch)
  - **Status**: ✅ Healthy
  - **CPU Load**: 7% | **Memory Util**: 18%
  - **Interfaces**: port1 (UP), port2 (UP), port3 (UP)
  - **Traffic**: ↔️ 80 Mbps Aggregate
- **Node**: `Server-App01` (IP: 192.168.1.10, Type: Server)
  - **Status**: ✅ Up
  - **Connected To**: Switch-Core (via port3)
  - **Traffic**: ➡️ 15 Mbps (to Internet) / ⬅️ 5 Mbps (from Clients)

## Live Charts Pane:
(Interactive charts showing historical and real-time data)
- **Global Bandwidth Usage**: [Line Graph: Total Ingress vs. Egress over last 5 minutes]
  - Peak Ingress: 120 Mbps | Peak Egress: 90 Mbps
- **Device CPU Load**: [Bar Chart: CPU % for Router-Edge, Switch-Core, etc.]

## Packet Details Panel (on selecting a specific flow):
- **Source IP**: 192.168.1.10
- **Destination IP**: 8.8.8.8 (Google DNS)
- **Protocol**: UDP
- **Source Port**: 54321
- **Destination Port**: 53 (DNS)
- **Payload Snippet**: [DNS Query for example.com]
- **Timestamp**: 2023-10-27 10:30:15.123
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) [Year] [Your Name or Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```