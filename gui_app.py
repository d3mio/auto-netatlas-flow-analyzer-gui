import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class NetworkVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("NetAtlas Flow Analyzer")
        self.root.geometry("1200x800")
        self.setup_styles()
        self.create_widgets()
        self.network_graph = nx.Graph()
        self.update_graph()
        
    def setup_styles(self):
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.style.configure(".", background="#2e2e2e", foreground="white")
        self.style.configure("TFrame", background="#2e2e2e")
        self.style.configure("TLabel", background="#2e2e2e", foreground="white")
        self.style.configure("TButton", background="#3a3a3a", foreground="white")
        self.style.map("TButton", background=[("active", "#4a4a4a")])
        self.style.configure("TEntry", fieldbackground="#3a3a3a", foreground="white")
        self.style.configure("TCombobox", fieldbackground="#3a3a3a", foreground="white")
        
    def create_widgets(self):
        # Main frames
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        graph_frame = ttk.Frame(self.root)
        graph_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Control panel
        ttk.Label(control_frame, text="NetAtlas Controls", font=('Helvetica', 14, 'bold')).pack(pady=(0, 20))
        
        # Device management
        device_frame = ttk.LabelFrame(control_frame, text="Device Management", padding="10")
        device_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(device_frame, text="Device IP:").grid(row=0, column=0, sticky=tk.W)
        self.ip_entry = ttk.Entry(device_frame)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(device_frame, text="Device Type:").grid(row=1, column=0, sticky=tk.W)
        self.device_type = ttk.Combobox(device_frame, values=["Router", "Switch", "Server", "Firewall", "Workstation"])
        self.device_type.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Button(device_frame, text="Add Device", command=self.add_device).grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.EW)
        ttk.Button(device_frame, text="Remove Device", command=self.remove_device).grid(row=3, column=0, columnspan=2, sticky=tk.EW)
        
        # Connection management
        conn_frame = ttk.LabelFrame(control_frame, text="Connections", padding="10")
        conn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(conn_frame, text="From:").grid(row=0, column=0, sticky=tk.W)
        self.from_device = ttk.Combobox(conn_frame)
        self.from_device.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(conn_frame, text="To:").grid(row=1, column=0, sticky=tk.W)
        self.to_device = ttk.Combobox(conn_frame)
        self.to_device.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Button(conn_frame, text="Connect Devices", command=self.connect_devices).grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.EW)
        ttk.Button(conn_frame, text="Disconnect Devices", command=self.disconnect_devices).grid(row=3, column=0, columnspan=2, sticky=tk.EW)
        
        # Traffic simulation
        traffic_frame = ttk.LabelFrame(control_frame, text="Traffic Simulation", padding="10")
        traffic_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(traffic_frame, text="Simulate Traffic", command=self.simulate_traffic).pack(fill=tk.X, pady=2)
        ttk.Button(traffic_frame, text="Clear Traffic", command=self.clear_traffic).pack(fill=tk.X, pady=2)
        
        # Status information
        status_frame = ttk.LabelFrame(control_frame, text="Network Status", padding="10")
        status_frame.pack(fill=tk.X, pady=5)
        
        self.network_status = ttk.Label(status_frame, text="Devices: 0 | Connections: 0 | Traffic: Idle")
        self.network_status.pack()
        
        # Graph canvas
        self.fig = plt.Figure(figsize=(8, 6), dpi=100, facecolor="#2e2e2e")
        self.ax = self.fig.add_subplot(111, facecolor="#2e2e2e")
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)
        
    def add_device(self):
        ip = self.ip_entry.get()
        dev_type = self.device_type.get()
        
        if not ip or not dev_type:
            messagebox.showwarning("Input Error", "Please enter both IP and device type")
            return
            
        self.network_graph.add_node(ip, type=dev_type, traffic=0)
        self.update_device_combos()
        self.update_graph()
        messagebox.showinfo("Success", f"Device {ip} ({dev_type}) added to network")
        
    def remove_device(self):
        ip = self.ip_entry.get()
        if not ip:
            messagebox.showwarning("Input Error", "Please enter an IP to remove")
            return
            
        if ip not in self.network_graph.nodes:
            messagebox.showwarning("Error", "Device not found in network")
            return
            
        self.network_graph.remove_node(ip)
        self.update_device_combos()
        self.update_graph()
        messagebox.showinfo("Success", f"Device {ip} removed from network")
        
    def update_device_combos(self):
        devices = list(self.network_graph.nodes)
        self.from_device['values'] = devices
        self.to_device['values'] = devices
        
    def connect_devices(self):
        from_dev = self.from_device.get()
        to_dev = self.to_device.get()
        
        if not from_dev or not to_dev:
            messagebox.showwarning("Input Error", "Please select both source and destination devices")
            return
            
        if from_dev == to_dev:
            messagebox.showwarning("Input Error", "Cannot connect a device to itself")
            return
            
        self.network_graph.add_edge(from_dev, to_dev, traffic=0)
        self.update_graph()
        messagebox.showinfo("Success", f"Connection established between {from_dev} and {to_dev}")
        
    def disconnect_devices(self):
        from_dev = self.from_device.get()
        to_dev = self.to_device.get()
        
        if not from_dev or not to_dev:
            messagebox.showwarning("Input Error", "Please select both source and destination devices")
            return
            
        if not self.network_graph.has_edge(from_dev, to_dev):
            messagebox.showwarning("Error", "No connection exists between these devices")
            return
            
        self.network_graph.remove_edge(from_dev, to_dev)
        self.update_graph()
        messagebox.showinfo("Success", f"Connection removed between {from_dev} and {to_dev}")
        
    def simulate_traffic(self):
        if not self.network_graph.edges:
            messagebox.showwarning("Error", "No connections available to simulate traffic")
            return
            
        for edge in self.network_graph.edges:
            self.network_graph.edges[edge]['traffic'] = random.randint(1, 100)
            
        for node in self.network_graph.nodes:
            connected_traffic = sum(self.network_graph.edges[edge]['traffic'] for edge in self.network_graph.edges if node in edge)
            self.network_graph.nodes[node]['traffic'] = min(connected_traffic, 100)
            
        self.update_graph()
        messagebox.showinfo("Success", "Traffic simulation completed")
        
    def clear_traffic(self):
        for edge in self.network_graph.edges:
            self.network_graph.edges[edge]['traffic'] = 0
            
        for node in self.network_graph.nodes:
            self.network_graph.nodes[node]['traffic'] = 0
            
        self.update_graph()
        messagebox.showinfo("Success", "All traffic cleared")
        
    def update_graph(self):
        self.ax.clear()
        
        if not self.network_graph.nodes:
            self.ax.text(0.5, 0.5, "No network devices\nAdd devices to begin", 
                        ha='center', va='center', color='white', fontsize=12)
            self.canvas.draw()
            self.update_status()
            return
            
        # Node colors based on type
        node_colors = []
        for node in self.network_graph.nodes:
            node_type = self.network_graph.nodes[node]['type']
            traffic_level = self.network_graph.nodes[node]['traffic']
            
            if node_type == "Router":
                node_colors.append((0, 0.8 - 0.007*traffic_level, 0.8 - 0.005*traffic_level))
            elif node_type == "Switch":
                node_colors.append((0.8 - 0.007*traffic_level, 0.8 - 0.005*traffic_level, 0))
            elif node_type == "Server":
                node_colors.append((0.8 - 0.007*traffic_level, 0, 0))
            elif node_type == "Firewall":
                node_colors.append((0.8 - 0.007*traffic_level, 0, 0.8 - 0.005*traffic_level))
            else:  # Workstation
                node_colors.append((0.8 - 0.007*traffic_level, 0.6 - 0.005*traffic_level, 0.2))
        
        # Edge colors based on traffic
        edge_colors = [
            plt.cm.Reds(min(0.3 + self.network_graph.edges[edge]['traffic']/150, 1))
            for edge in self.network_graph.edges
        ]
        
        # Draw the graph
        pos = nx.spring_layout(self.network_graph)
        
        # Draw edges with traffic-dependent width
        edge_widths = [1 + self.network_graph.edges[edge]['traffic']/20 for edge in self.network_graph.edges]
        nx.draw_networkx_edges(
            self.network_graph, pos, ax=self.ax,
            edge_color=edge_colors,
            width=edge_widths,
            alpha=0.7
        )
        
        # Draw nodes with type-dependent color and traffic effect
        node_sizes = [900 + 30*self.network_graph.nodes[node]['traffic'] for node in self.network_graph.nodes]
        nx.draw_networkx_nodes(
            self.network_graph, pos, ax=self.ax,
            node_color=node_colors,
            node_size=node_sizes,
            alpha=0.8
        )
        
        # Draw labels
        nx.draw_networkx_labels(
            self.network_graph, pos, ax=self.ax,
            font_size=8,
            font_color="white"
        )
        
        # Draw edge labels (traffic)
        edge_labels = {
            edge: f"{self.network_graph.edges[edge]['traffic']}%"
            for edge in self.network_graph.edges
        }
        nx.draw_networkx_edge_labels(
            self.network_graph, pos, ax=self.ax,
            edge_labels=edge_labels,
            font_size=7,
            font_color="white"
        )
        
        self.canvas.draw()
        self.update_status()
        
    def update_status(self):
        num_devices = len(self.network_graph.nodes)
        num_connections = len(self.network_graph.edges)
        total_traffic = sum(self.network_graph.edges[edge]['traffic'] for edge in self.network_graph.edges)
        
        if total_traffic == 0:
            traffic_status = "Idle"
        elif total_traffic < 30 * num_connections:
            traffic_status = "Low"
        elif total_traffic < 70 * num_connections:
            traffic_status = "Medium"
        else:
            traffic_status = "High"
            
        self.network_status.config(
            text=f"Devices: {num_devices} | Connections: {num_connections} | Traffic: {traffic_status}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkVisualizer(root)
    root.mainloop()